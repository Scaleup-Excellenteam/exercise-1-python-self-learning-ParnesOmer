def parsle_tongue(filename, chunk_size=1024):
    buffer = b''
    min_size = 5
    current_string = ""
    try:
        with open(filename, 'rb') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break

                buffer += chunk
                for char in chunk:
                    char = chr(char)
                    if char.isalpha() and char.islower() and char.isascii():
                        current_string += char
                    else:
                        if char == '!' and len(current_string) >= min_size:
                            current_string += char
                            yield current_string
                        current_string = ""

                    # שמור את חמשת הבתים האחרונים כדי לוודא שמחרוזת לא תתפצל בין נתחים
                    # buffer = buffer[-min_size:]

    except FileNotFoundError:
        print("The file was not found.")
    # except OSError:
    #     print("An error occurred while reading the file.")

if __name__ == "__main__":
    # Using a generator to read the file in parts
    filename = 'logo.jpg'
    gen = parsle_tongue(filename)
    for word in gen:
        print(word)