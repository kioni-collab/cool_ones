import datetime
from DBquery import valid_status_id

def safe_int(input_value: str, default_value: int) -> int:
    try:
        return int(input_value)
    except:
        return default_value


def safe_date(input_year: str, input_month: str, input_day: str, default_date: datetime):
    try:
        return datetime.datetime(int(input_year), int(input_month), int(input_day))
    except:
        return default_date

def safe_id(input_val:str, list_id:list):
    
    return input_val in list_id

