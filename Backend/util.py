def safe_int(input_value: str, default_value: int) -> int:
    try:
        return int(input_value)
    except:
        return default_value