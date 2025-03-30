"""
Module for reading an image and extracting an encrypted message embedded
using a specific encoding scheme. It retrieves characters from pixel data.
"""
from PIL import Image


def remember_remember(image_name):
    """
        Extracts an encrypted message embedded in an image.

        This function opens an image file, iterates through its pixels, and attempts
        to decode a hidden message based on pixel values. The function looks for a
        pixel value of 1 to extract corresponding characters.

        Parameters:
        image_name (str): The file path to the image containing the hidden message.

        Returns:
        str: The decrypted message embedded in the image.
        """
    try:
        with Image.open(image_name) as image:
            encrypted_message = []
            width, height = image.size
            for w in range(width):
                for h in range(height):
                    pixel = image.getpixel((w, h))
                    if pixel == 1:
                        encrypted_message.append(chr(h))
                        break
            return ''.join(encrypted_message)
    except FileNotFoundError:
        print(f"File not found: {image_name}")
        return ""  # Ensures that the function always returns a value


if __name__ == "__main__":
    print(remember_remember("code.png"))
