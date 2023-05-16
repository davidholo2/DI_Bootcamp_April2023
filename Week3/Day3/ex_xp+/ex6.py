from datetime import datetime


def minutes_lived(birthdate):
    current_datetime = datetime.now()
    age = current_datetime - birthdate
    minutes = age.total_seconds() / 60

    print(f"You have lived approximately {minutes:.2f} minutes.")


# Example usage
birthdate = datetime(2001, 7, 19)  # Replace with the birthdate of your choice
minutes_lived(birthdate)
