from dateutil.parser import parse
from datetime import datetime, timedelta

def add_days_to_date(date_str, days):
    """
    Add days to a date string and return a formatted date string.
    
    Args:
        date_str (str): Date string in any common format
        days (int): Number of days to add (can be negative)
    
    Returns:
        str: Formatted date string in YYYY-MM-DD format
    """
    try:
        date_obj = parse(date_str)
        new_date = date_obj + timedelta(days=days)
        return new_date.strftime('%Y-%m-%d')
    except ValueError as e:
        raise ValueError(f"Invalid date format: {date_str}") from e

def get_days_between(date1_str, date2_str):
    """
    Calculate the number of days between two date strings.
    
    Args:
        date1_str (str): First date string
        date2_str (str): Second date string
    
    Returns:
        int: Number of days between the two dates
    """
    try:
        date1 = parse(date1_str)
        date2 = parse(date2_str)
        return abs((date2 - date1).days)
    except ValueError as e:
        raise ValueError("Invalid date format") from e