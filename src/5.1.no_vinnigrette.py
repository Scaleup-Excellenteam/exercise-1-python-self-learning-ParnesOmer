import random
import datetime

def no_vinnigrete(start_date, end_date):
    """Generates a random date between start_date and end_date using epoch timestamps."""
    start_timestamp = int(datetime.datetime.strptime(start_date, "%Y-%m-%d").timestamp())
    end_timestamp = int(datetime.datetime.strptime(end_date, "%Y-%m-%d").timestamp())

    # Pick a random timestamp in the given range
    random_timestamp = random.randint(start_timestamp, end_timestamp)

    # Convert back to a date
    random_date = datetime.datetime.fromtimestamp(random_timestamp).strftime("%Y-%m-%d")

    # Check if the date falls on a Monday
    if datetime.datetime.fromtimestamp(random_timestamp).weekday() == 0:
        print("Ain't gettin' no vinaigrette today :(")

    return random_date

if __name__ == "__main__":
   print(no_vinnigrete("2023-07-10", "2023-07-10"))
