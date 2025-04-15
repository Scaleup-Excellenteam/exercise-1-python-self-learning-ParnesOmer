"""
Module: no_vinnigrete
Generates a random date within a given range and prints a message
if the selected date falls on a Monday.
"""
import random
import datetime

# Define a constant for Monday
MONDAY = 0
def no_vinnigrete(start_date, end_date):
    """
    Generates a random date between start_date and end_date.

    This function takes two date strings (in the format "YYYY-MM-DD")
    and print a random date within the specified range (inclusive).
    If the random date falls on a Monday, a specific message
    will be printed.

    Parameters:
    start_date (str or datetime): The start date (either a string in the
                                    format "YYYY-MM-DD" or a datetime object).
    end_date (str or datetime): The end date (either a string in the format
                                "YYYY-MM-DD" or a datetime object).
    """
    if isinstance(start_date, str):
        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    if isinstance(end_date, str):
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")

    start_date = min(start_date, end_date)
    end_date = max(end_date, start_date)
    difference = (end_date - start_date).days

    # Pick a random timestamp in the given range
    random_timestamp = random.randint(0, difference)
    result = start_date + datetime.timedelta(days=random_timestamp)
    # Check if the date falls on a Monday
    if result.weekday() == MONDAY:
        print("Ain't gettin' no vinaigrette today :(")
    

if __name__ == "__main__":
    # Get user input
    date1 = input("Enter the first date (YYYY-MM-DD): ")
    date2 = input("Enter the second date (YYYY-MM-DD): ")
    no_vinnigrete(date1, date2)
