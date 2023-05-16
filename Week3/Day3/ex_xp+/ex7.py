from datetime import datetime


def display_today_and_next_holiday():
    today = datetime.now()
    upcoming_holiday = datetime(2023, 6, 4)
    time_left = upcoming_holiday - today
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"Today's date and time is: {today}")
    print(
        f"The next holiday is in {days} days, {hours:02}:{minutes:02}:{seconds:02} hours.")
    print("The next holiday is: Shavout")


display_today_and_next_holiday()
