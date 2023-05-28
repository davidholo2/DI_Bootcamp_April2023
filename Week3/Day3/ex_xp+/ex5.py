from datetime import datetime


def time_until_january_1st():
    current_datetime = datetime.now()
    target_datetime = datetime(current_datetime.year + 1, 1, 1)
    time_left = target_datetime - current_datetime
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(
        f"The 1st of January is in {days} days, {hours:02}:{minutes:02}:{seconds:02} hours.")


time_until_january_1st()
