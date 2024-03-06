import sys
from PIL import Image, ImageOps
import os

def resize_and_overlay(input_path, output_path):
    shirt = Image.open("shirt.png")

    try:
        input_image = Image.open(input_path)

    except FileNotFoundError:
        print("Input does not exist")
        sys.exit(1)

    input_image = ImageOps.fit(input_image, shirt.size)
    input_image.paste(shirt, shirt)
    input_image.save(output_path)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        input_path = sys.argv[1]
        output_path = sys.argv[2]

        valid_extensions = {'.jpg', '.jpeg', '.png'}
        _, input_ext = os.path.splitext(input_path)
        _, output_ext = os.path.splitext(output_path)

        if not (input_ext.lower() in valid_extensions and output_ext.lower() in valid_extensions):
            print("Invalid output")
            sys.exit(1)

        if not os.path.exists(input_path):
            print(f"Input does not exist.")
            sys.exit(1)

        if input_ext.lower() != output_ext.lower():
            print("Input and output have different extensions")
            sys.exit(1)

        resize_and_overlay(input_path, output_path)
