"""
DOC: Includes general utility tools,
checking if objects are nonetypes or the corect ones
"""
import datetime
from DBquery import valid_status_id
#TODO: remove import valid_status_ID once done, if not needed

def safe_int(input_value: str, default_value: int) -> int:
    """
    Explicitly casts the input into an Int, if it ifails, returns a default value
    that was inputted. The pylint disable bare is there because the Except
    statement has no explicit exception, so instead of writing
    a new except for each exception, just say all excepts and get pythong
    to not yell at us for it
    """
    try:
        return int(input_value)
    except: # pylint: disable=bare-except
        return default_value


def safe_date(input_year: str, input_month: str, input_day: str, default_date: datetime):
    """
    Explicitly casts the Month, year, and day into a DateTime, and if it fails,
    returns a default date provided, see above for disable exception explanation
    """
    try:
        return datetime.datetime(int(input_year), int(input_month), int(input_day))
    except: # pylint: disable=bare-except
        return default_date

def safe_id(input_val:str, list_id:list):
    """
    Checks if the given input value is in the given list, returning it if it is
    """
    return input_val in list_id
