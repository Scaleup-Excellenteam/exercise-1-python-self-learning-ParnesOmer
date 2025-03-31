"""
Module to group elements from an iterable based on the result of a function applied to each element.
This function returns a dictionary where keys are the results of applying the function,
and values are lists of elements that correspond to each key.
"""


def group_by(f, iterator):
    """
    Groups elements of the iterator based on the function f.
    Parameters:
    f (function): function
    iterator (iterable): An iterable of elements to be grouped.
    Returns:
    dict: A dictionary where the keys are the results of the function f and the values are lists
          of elements from the iterator that correspond to each key.
    """
    try:
        my_dict = {}
        for i in iterator:
            value = f(i)
            if value in my_dict:
                my_dict[value].append(i)
            else:
                my_dict[value] = [i]
        return my_dict
    except ValueError as e:
        print(f"Error: {e}")
        return {}
    except TypeError as e:
        print(f"Error: {e}")
        return {}
    # the tests don't allow me to write:
    # except Exception as e:
    #     print(f"Unexpected error: {e}")
    #     return {}

if __name__ == "__main__":
    print(group_by(len, ["hi", "bye", "yo", "try"]))
