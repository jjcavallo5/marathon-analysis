def fmt_seconds(seconds: int) -> str:
    minutes = seconds // 60
    seconds_remaining = seconds % 60

    hours = minutes // 60
    minutes_remaining = minutes % 60

    return f'{hours}:{minutes_remaining:02d}:{seconds_remaining:02d}'
