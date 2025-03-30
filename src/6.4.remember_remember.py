# remember_remember
from PIL import Image
def remember_remember(image_name):
    try:
        with Image.open(image_name) as image:
            Encrypted_message = []
            width, height = image.size
            for w in range(width):
                for h in range(height):
                    pixel = image.getpixel((w, h))
                    if pixel == 1:
                        Encrypted_message.append(chr(h))
                        break
            return ''.join(Encrypted_message)
    except FileNotFoundError:
        print(f"File not found: {image_name}")

if __name__ == "__main__":
    print(remember_remember("code.png"))