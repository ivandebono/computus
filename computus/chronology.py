def indiction(year: int, calendar: str = "AD") -> int:
    """
    Calculate the indiction number (1–15).

    Parameters:
        year (int): Year in AD
        calendar (str): 'AD' or 'AM'

    Returns:
        int: Indiction number
    """

    if calendar == "AD":
        return ((year + 2) % 15) + 1

    elif calendar == "AM":
        am = year + 5508
        ind = am % 15
        return 15 if ind == 0 else ind

    else:
        raise ValueError("calendar must be 'AD' or 'AM'")