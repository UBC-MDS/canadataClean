def clean_postalcode(text: str, region: str = None) -> str:
    """
    Clean and validate a free-text entry representing a Canadian postal code and convert it to the standard Canadian postal code format "A1A 1A1".

    The function accepts postal codes in a variety of formats, including with or without spaces, dashes, or lowercase letters. It first removes extraneous characters and normalizes the string to uppercase. If a `region` is provided, the function checks that the postal code matches the expected prefix for that province or territory. The postal code is then reformatted to the standard "A1A 1A1" format. If the postal code is invalid or does not match the specified region, a ValueError is raised.
    
    Parameters
    ----------
    text : str
        The input string representing a Canadian postal code.
    region : str, optional
        The Canadian province or territory to validate the postal code against (default is None, which skips region-specific validation).

    Returns
    -------
    str
        The validated Canadian postal code in standard "A1A 1A1" format.

    Raises
    ------
    ValueError
        If the input does not match a valid Canadian postal code pattern,
        or if it does not match the specified region's postal code prefix.

    Examples
    --------
    >>> clean_postalcode("K1A0B1")
    'K1A 0B1'
    >>> clean_postalcode("k1a 0b1", region="ON")
    'K1A 0B1'
    >>> clean_postalcode("V5K0A1", region="ON")
    # Raises ValueError: Postal code does not match the specified region
    >>> clean_postalcode("12345")
    # Raises ValueError: Invalid Canadian postal code
    """