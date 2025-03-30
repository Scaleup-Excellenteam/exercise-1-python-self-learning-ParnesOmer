def generator_interleave(*iterables):
    """
    Intertwine elements from multiple iterables using a generator.
    This function takes one or more iterable objects and returns a generator
    that yields their elements in an interleaved fashion.

    Parameters:
    *iterables: One or more iterable objects (e.g., lists, tuples, strings).

    Yields:
    The next interleaved element from the input iterables, one at a time.
    """
    # Convert each iterable to an iterator
    iterators = [iter(it) for it in iterables]
    # Continue until there are no more iterators
    while iterators:
        # Iterate over each iterator
        for it in iterators:
            try:
                # Yield the next item from the iterator
                yield next(it)
            except StopIteration:
                # If the iterator is exhausted, remove it from the list
                iterators.remove(it)
def interleave(*iterables):
     """
    Intertwine elements from multiple iterables and return a list.
   
    Parameters:
    *iterables: One or more iterable objects (e.g., lists, tuples, strings).

    Returns:
    A list of interleaved elements from the input iterables.
    """
    # Convert each iterable to an iterator
    iterators = [iter(it) for it in iterables]
    final_list = []
    # Continue until there are no more iterators
    while iterators:
        # Iterate over each iterator
        for it in iterators:
            try:
                # Append the next item from the iterator
                final_list.append(next(it))
            except StopIteration:
                # If the iterator is exhausted, remove it from the list
                iterators.remove(it)
    return final_list

if __name__ == '__main__':
    result = list(generator_interleave('abc', [1, 2, 3], ('!', '@', '#')))
    result2 = interleave('abc', [1, 2, 3], ('!', '@', '#'))
    print(result)
    print(result2)
