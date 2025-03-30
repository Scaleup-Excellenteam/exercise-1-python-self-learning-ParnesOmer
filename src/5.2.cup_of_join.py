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
    if not lists:
        return None  # If no lists are provided, return None

    result = []
    for i, lst in enumerate(lists):
        if i > 0 and sep is not None:
            result.append(sep)  # Add separator between lists
        result.extend(lst)  # Add elements of the current list

    if sep:
        result.append(sep)  # Add separator between lists
    return result


if __name__ == "__main__":
    # Test cases
    print(cup_of_join([], [1], [], sep='x'))
