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
        print("אין לי ויניגרט!")

    return random_date

if __name__ == "__main__":
    # Get user input
    date1 = input("Enter the first date (YYYY-MM-DD): ")
    date2 = input("Enter the second date (YYYY-MM-DD): ")
    print("Random date:", no_vinnigrete(date1, date2))