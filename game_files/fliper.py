import os

from PIL import Image

def flip_image_vertical(input_path, output_path):
    original_image = Image.open(input_path)
    flipped_image = original_image.transpose(Image.FLIP_LEFT_RIGHT)
    flipped_image.save(output_path)

def rename_format(input_path, output_path):
    original_image = Image.open(input_path)
    flipped_image = original_image.transpose(Image.FLIP_LEFT_RIGHT)
    flipped_image.save(output_path)
    os.system(f"rm {input_path}")

if __name__ == "__main__":
    for i in range(38):
        input_path = f"images/dios_right/{i}.png"
        output_path = f"images/dios_left/{i}.png"

        flip_image_vertical(input_path, output_path)