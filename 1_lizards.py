SECONDS_IN_MINUTE = 60
MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24
DAYS_IN_YEAR = 365
SECONDS_IN_HOUR = SECONDS_IN_MINUTE * MINUTES_IN_HOUR
SECONDS_IN_DAY = SECONDS_IN_HOUR * HOURS_IN_DAY
DAYS_IN_MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def date_to_seconds(date: list[int]) -> int:
    """Convert date to seconds."""
    year, month, day, hour, minute, second = date
    days = year * DAYS_IN_YEAR + sum(DAYS_IN_MONTHS[:month - 1]) + day
    return days * SECONDS_IN_DAY + hour * SECONDS_IN_HOUR + minute * SECONDS_IN_MINUTE + second


def calculate_time_difference(start_date: list[int], end_date: list[int]) -> tuple[int, int]:
    """Calculate time difference."""
    seconds_difference = date_to_seconds(end_date) - date_to_seconds(start_date)
    return divmod(seconds_difference, SECONDS_IN_DAY)


def read_input() -> tuple[list[int], list[int]]:
    """Read input data."""
    start_date = list(map(int, input().split()))
    end_date = list(map(int, input().split()))
    return start_date, end_date


if __name__ == "__main__":
    start_date, end_date = read_input()
    total_days, seconds_remaining = calculate_time_difference(start_date, end_date)
    print(total_days, seconds_remaining)
