def clean_date(text: str) -> str:
    """
    Clean and validate a date string, converting common formats to the Canadian standard YYYY-MM-DD (ISO 8601).

    The function accepts date strings in the following formats:
    - YYYY-MM-DD (primary target format)
    - DD/MM/YYYY (common in many countries, or areas that are highly influence by the British)
    - DD-MM-YYYY

    It performs the following steps:
    1. Strips leading/trailing whitespace.
    2. Attempts to parse the input using the supported formats.
    3. If parsing succeeds, reformats the date to YYYY-MM-DD.
    4. Validates that the resulting date is not in the future (i.e., on or before today's date).
    5. Validates that the date is plausible (e.g., year reasonable for a living person, typically 1900 or later).
    6. Validates that the date is complete (e.g., No February 30)

    Parameters
    ----------
    text : str
        The input string representing a date in one of the supported formats.

    Returns
    -------
    str
        The validated date in strict YYYY-MM-DD format.

    Raises
    ------
    ValueError
        If the input cannot be parsed as a valid date in any supported format,
        if the resulting date is in the future,
        or if the date is otherwise invalid (e.g., February 30).

    Examples
    --------
    >>> clean_date("1990-05-15")
    '1990-05-15'
    >>> clean_date("15/05/1990")
    '1990-05-15'
    >>> clean_date("15-05-1990")
    '1990-05-15'
    >>> clean_date("  15 / 05 / 1990  ")
    '1990-05-15'
    >>> clean_date("2030-01-01")  # Future date
    # Raises ValueError: Date cannot be in the future
    >>> clean_date("February 30")
    # Raises ValueError: Unable to parse date
    """
