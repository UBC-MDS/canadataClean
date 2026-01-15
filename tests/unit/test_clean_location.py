"""
A test module for the location cleaning functions.
"""
import pytest
import re
from canadata_clean.clean_location import clean_location
from canadata_clean.clean_location import remove_punctuation
from canadata_clean.clean_location import remove_spaces



def test_clean_location():
    """
    Run the following tests to ensure that the clean_location function works as expected.
    """

    empty()
    output_type()
    incomplete_input()
    capitalization()
    spaces_sides()
    spaces_middle()
    format()
    unidentified_province_territory()
    province_territory_replacement()
    same_distance_raises_error()

def empty():
    """
    Test that the function never returns an empty string.
    """

    assert clean_location("BC"), "Output should not be empty."
 
def capitalization():
    """
    Test that the output is always capitalized.
    """

    out = clean_location("bc")
    expected_out = "BC"
    assert out == expected_out, f"Expected {expected_out} but got {out}"

def spaces_sides():
    """
    Test that the output string starts and ends in a non-space character.
    """

    out = clean_location("  manitoba   ")
    assert not out.startswith(" "), "Output should not begin with a space."
    assert not out.endswith(" "), "Output should not end with a space."

def spaces_middle():
    """
    Test that the output string does not have more than one space between characters.
    """

    assert not re.search(r" {2,}", clean_location("Newfoundland  and.   Labrador"))
    assert not re.search(r" {2,}", clean_location("Newfoundlandandlabrador"))
    assert not re.search(r" {2,}", clean_location("Newfoundland and Labrador"))

def format():
    """
    Test that the output is of the format '<two-letter code>'.
    """

    assert re.match(r"^[A-Z]{2}$", clean_location("Ont."))
    assert re.match(r"^[A-Z]{2}$", clean_location("New Brunswich"))
    assert re.match(r"^[A-Z]{2}$", clean_location("Saskatchewan"))
    assert re.match(r"^[A-Z]{2}$", clean_location("Yukon"))

def output_type():
    """
    Test that the output is of type string.
    """

    # output should be string if something was modified
    assert isinstance(clean_location("City BC"), str)
    # output should be string if nothing was modified
    assert isinstance(clean_location("City, BC"), str)

def wrong_input_type():
    """
    Test that a non-string input type throws a TypeError.
    """

    with pytest.raises(TypeError):
        clean_location(123)
    
    with pytest.raises(TypeError):
        clean_location(1.1)

    with pytest.raises(TypeError):
        clean_location(True)
    
    with pytest.raises(TypeError):
        clean_location(["First Location", "Second Location"])

def incomplete_input():
    """
    Test that empty strings throw a ValueError.
    """

    with pytest.raises(ValueError):
        clean_location("")
    
    with pytest.raises(ValueError):
        clean_location(" ")

def province_territory_replacement():
    """
    Test that the function correctly matches various province/territory names and abbreviations to the official two-letter code, including small and medium typos.
    """

    testing_province_territory_replacement = {
        "british columbia": "BC", # case insensitive
        "Ont.": "ON", # periods at end
        "P.E.I": "PE", # periods between letters
        "Prince Edward Isl.": "PE", # uncommon abbreviations that are close enough to the full name
        "Saskatch.": "SK", # uncommon abbreviations that are close enoguh to the full name
        "Nfld. Lab.": "NL", # multiple abbreviations for the same province/territory
        "Alberts": "AB", # small typos
        "siskachwin": "SK", # medium typos
        "north ws territry": "NT", # medium typos
        "brit columbia": "BC", # unknown abbreviations
        "newfoundlandandlabrador": "NL", # no spaces in text input
        "newfoundland": "NL", # incomplete text input
        "qc": "QC", # minimum valid input
        "Prince-Edward-Island": "PE", # hyphens between letters
        "Newfoundland & Labrador": "NL" # other punctuation
    }

    for key, value in testing_province_territory_replacement.items():
        out = clean_location(key)
        assert out == value, f"Expected {value} but got {out}"

def same_distance_raises_error():
    """
    Test that the function raises a ValueError if the input has equal
    partial matches to two or more province/territories.
    """
    with pytest.raises(ValueError):
        clean_location("VB")

def unidentified_province_territory():
    """
    Test that the function throws a ValuError if it cannot identify a province/territory, including significant typos.
    """

    with pytest.raises(ValueError):
        clean_location("XX")
    
    with pytest.raises(ValueError):
        clean_location("C")

    with pytest.raises(ValueError):
        clean_location("Not A Province")

    with pytest.raises(ValueError):
        clean_location("alllbita")

    with pytest.raises(ValueError):
        clean_location("b colum")

# Added additional tests for remove_punctuation and remove_spaces helper functions as suggested by ChatGPT. I wrote the tests myself: ChatGPT only provided the suggestion that I test these functions independently.
def test_remove_punctuation():
    """
    Test that the helper function remove_punctuation works as expected.
    """
    assert remove_punctuation("P.E.I.") == "PEI"
    assert remove_punctuation("N.-W.-T.") == "NWT"
    assert remove_punctuation("Prince-Edward-Island") == "PrinceEdwardIsland"
    assert remove_punctuation("Newfoundland & Labrador") == "Newfoundland  Labrador"

def test_remove_spaces():
    """
    Test that the helper function remove_spaces works as expected.
    """
    assert remove_spaces("newfoundland and labrador") == "newfoundlandandlabrador"
    assert remove_spaces("newfoundland and      labrador") == "newfoundlandandlabrador"