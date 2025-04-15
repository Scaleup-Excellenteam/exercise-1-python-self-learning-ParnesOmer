"""
Module to read a binary file and extract sequences of lowercase alphabetical characters
ending with '!' character. The sequences must be at least 5 characters long.

This module contains the function `parsle_tongue` which reads a file in chunks and yields
sequences of valid characters as described above.

Raises:
FileNotFoundError: If the specified file is not found.
"""

# Define constants
MIN_SIZE = 5  # Minimum size of valid sequences
CHUNK_SIZE = 1024  # Size of each chunk read from the file
FILENAME = 'logo.jpg'  # Name of the file to read
def parsle_tongue():
    """
        Reads a binary file in chunks and yields sequences of lowercase alphabetical
        characters that end with the '!' character, the
        sequence is at least 5 characters long.

        Yields:
        str: A sequence of lowercase alphabetical characters followed by a '!' character.

        Raises:
        FileNotFoundError: If the specified file is not found.
        """
    buffer = b''  # Buffer to hold the current chunk and last characters
    current_string = ""
    with open(FILENAME, 'rb') as file:
        while True:
            chunk = file.read(CHUNK_SIZE)
            if not chunk:
                break
            buffer += chunk
            for char in buffer:
                char = chr(char)
                if char.isalpha() and char.islower() and char.isascii():
                    current_string += char
                else:
                    if char == '!' and len(current_string) >= MIN_SIZE:
                        yield current_string
                    current_string = ""
            # This line ensures that only the last 'MIN_SIZE' characters are kept in the buffer
            # so that strings don't get split between chunks.
            buffer = buffer[-MIN_SIZE:]


if __name__ == "__main__":
    # Using a generator to read the file in parts
    try:
        gen = parsle_tongue()
        for word in gen:
            print(word)
    except FileNotFoundError:
        print(f"Error: The file '{FILENAME}' was not found.")
