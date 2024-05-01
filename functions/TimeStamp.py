import datetime
import calendar


def Get_Time_Stamp() -> str:
    timestamp = datetime.datetime.today()
    return str(timestamp)


def generate_analytics(timestamp: str, get_full_analytics: bool or None) -> dict:
    # Convert timestamp string to datetime object
    dt_object = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")

    # Get current time
    time = dt_object.strftime("%H:%M:%S")

    # Extract year, month, and day
    year = dt_object.year
    month_number = dt_object.month
    day = dt_object.day

    # Get full date
    full_date_words = dt_object.strftime("%A, %B %d, %Y")
    full_date_numbers = dt_object.strftime("%Y-%m-%d")

    # Get month in words
    month_in_words = dt_object.strftime("%B")

    analytics = {
        'full_date_in_words': full_date_words,
        'full_date_in_numbers': full_date_numbers,
        'time': time,
        'timestamp': timestamp,
        'year': year,
        'month_number': month_number,
        'day': day,
        'month_in_words': month_in_words
    } if get_full_analytics else {
        'full_date_in_words': full_date_words,
        'full_date_in_numbers': full_date_numbers,
        'time': time,
        'timestamp': timestamp
    }

    return analytics
