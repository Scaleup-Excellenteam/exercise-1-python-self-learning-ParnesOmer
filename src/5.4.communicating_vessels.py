"""
Module for interleaving elements from multiple iterables.

Provides two functions:
- generator_interleave: A generator that yields interwoven elements.
- interleave: Returns a list of interwoven elements.

Both functions take one or more iterable objects and yield/return their elements interleaved.
"""

from itertools import zip_longest

def generator_interleave(*iterables):
    """
       Intertwine iterators elements from multiple iterables.
       This function takes one or more iterable objects and returns a generator
       that yields their elements Intertwine. For example, given iterables
       Parameters:
       *iterables: One or more iterable objects (e.g., lists, tuples, strings).
       Yields:
       The next interleaved element from the input iterables.
       """
    # Use zip_longest to interleave elements from all iterables
    for elements in zip_longest(*iterables, fillvalue=None):
        for element in elements:
            if element is not None:
                yield element


def interleave(*iterables):
    """
       Intertwine iterators elements from multiple iterables.
       This function takes one or more iterable objects and returns a generator
       that yields their elements Intertwine. For example, given iterables
       Parameters:
       *iterables: One or more iterable objects (e.g., lists, tuples, strings).
       Yields:
       The next interleaved element from the input iterables.
       """
    # Use list comprehension with zip_longest to generate the interleaved list
    return [element for elements in zip_longest(*iterables, fillvalue=None) for element in elements if element is not None]



if __name__ == '__main__':
    result = list(generator_interleave('abc', [1, 2, 3], ('!', '@', '#')))
    result2 = interleave('abc', [1, 2, 3], ('!', '@', '#'))
    print(result)
    print(result2)
