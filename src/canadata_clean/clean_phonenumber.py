def clean_phonenumber(text: str) -> str:
    """
    Clean and validate a free-text entry phone number and convert it to the standard Canadian format "+1 (XXX) XXX-XXXX".

    The function accepts phone number in a variety of formats, including with or without parentheses, spaces, dashes, or a Canadian country code. 

    Parameters
    ----------
    text : str
        The input string representing a Canadian phone number.

    Returns
    -------
    text: str
        The validated Canadian phone number in standard "+1 (XXX) XXX-XXXX" format.
    
    Raises
    ------
    ValueError
        If the input does not contain exactly 10 digits (excluding the country code).
    

    Examples
    --------
    >>> clean_phonenumber("1-123-456-7890")
    '+1 (123) 456-7890'
    >>> clean_phonenumber("1234567890")
    '+1 (123) 456-7890'
    >>> clean_phonenumber("(123) 456-7890")
    '+1 (123) 456-7890'
    >>> clean_phonenumber("123 456 7890")
    '+1 (123) 456-7890'
    >>> clean_phonenumber("123456")
    # Raises ValueError: Invalid phone number length
    """

