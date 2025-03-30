"""
Module to measure the execution time of a given function.

This module provides the `running_2000` function to time the execution of a 
function with positional and keyword arguments.
"""
import time


def running_2000(f, *parameters, **keywords):
    """
    Measures the execution time of a given function.

    Parameters:
    f (function): The function to be executed and timed.
    *parameters: Positional arguments to pass to the function.
    **keywords: Keyword arguments to pass to the function.

    Returns:
    float: The execution time in seconds.
    """
    t_start = time.time()
    try:
        f(*parameters, **keywords)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
    t_end = time.time()
    return t_end - t_start


if __name__ == "__main__":
    print(running_2000(print, "Hello"))  # Example usage: measuring print execution time
