def parsle_tongue(filename='logo.jpg', chunk_size=1024):
    """
        Reads a binary file in chunks and yields sequences of lowercase alphabetical
        characters that end with the '!' character, the
        sequence is at least 5 characters long.

        Parameters:
        filename (str): The path to the file to be read.
        chunk_size (int): The size of the chunks to read at a time (default is 1024 bytes).

        Yields:
        str: A sequence of lowercase alphabetical characters followed by a '!' character.

        Raises:
        TypeError('filename cannot be None')
        FileNotFoundError: If the specified file is not found.
        """
    buffer = b''  # Buffer to hold the current chunk and last characters
    min_size = 5
    current_string = ""
    try:
        with open(filename, 'rb') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                buffer += chunk
                for char in buffer:
                    char = chr(char)
                    if char.isalpha() and char.islower() and char.isascii():
                        current_string += char
                    else:
                        if char == '!' and len(current_string) >= min_size:
                            yield current_string
                        current_string = ""
                # This line ensures that only the last 'min_size' characters are kept in the buffer
                # so that strings don't get split between chunks.
                buffer = buffer[-min_size:]

    except FileNotFoundError:
        print("The file was not found.")


if __name__ == "__main__":
    # Using a generator to read the file in parts
    filename = 'logo.jpg'
    gen = parsle_tongue(filename)
    for word in gen:
        print(word)
