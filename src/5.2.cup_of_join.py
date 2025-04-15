"""
Module: Implements the cup_of_join function.
This function joins multiple lists into a single list, adding a separator between them.
"""


def cup_of_join(*lists, sep=None):
    """
      Joins multiple lists into one, inserting a separator between them.

      Parameters:
      *lists: Lists to be joined.
      sep (str, optional): Separator to insert between lists. Default is "-".

      Returns:
      list: A single list containing all elements from input lists, separated by `sep`.
      """
    result = []
    separator = [sep] if sep is not None else []  # Predetermine the separator as a list
    for i, lst in enumerate(lists):
        if i > 0:
            result.extend(separator)  # Add separator between lists
        result.extend(lst)  # Add elements of the current list

    # Add separator at the end if there's only one list
    if separator is not None:
        result.extend(separator)
    return result

if __name__ == "__main__":
    # Test cases
    print(cup_of_join([], [1], [], sep='x'))
