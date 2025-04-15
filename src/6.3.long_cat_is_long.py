"""
Module to count the length of each word in a given text,
returning a dictionary where the keys are the words
and the values are their lengths.
"""


def long_cat_is_long(text):
    """
    Count the length of each word in the given text.

    Parameters:
    text (str): The input text to process.

    Returns:
    dict: A dictionary where the keys are words and the values are their lengths.
    """
    word_list = [''.join([char.lower() for char in word if char.isalpha()]) for word in text.split()]
    return {word: len(word) for word in word_list if word}

if __name__ == '__main__':
    if long_cat_is_long("bla bla tralala 123") == {'bla': 3, 'tralala': 7}:
        print('Correct!')
