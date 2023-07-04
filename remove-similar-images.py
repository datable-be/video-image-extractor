# This script will search for similar images (e.g. images extracted from a video file).
# All quasi duplicate images will be moved to a subfolder in the output_folder

import os
import shutil
from PIL import Image

input_folder = 'extracted_images/video-1'
output_folder = input_folder + '_dupes'
threshold = 5
image_hashes = {}
### Create a directory to save the extracted images
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


def dhash(image, hash_size = 8):
    # Compute the difference hash of an image.

    # Resize the image and convert it to grayscale.
    image = image.convert('L').resize((hash_size + 1, hash_size), Image.ANTIALIAS)
    # Calculate the difference between adjacent pixels.
    difference = []
    for row in range(hash_size):
        for col in range(hash_size):
            pixel_left = image.getpixel((col, row))
            pixel_right = image.getpixel((col + 1, row))
            difference.append(pixel_left > pixel_right)
    # Convert the binary difference to a hexadecimal hash string.
    decimal_value = 0
    hex_string = []
    for index, value in enumerate(difference):
        if value:
            decimal_value += 2 ** (index % 8)
        if (index % 8) == 7:
            hex_string.append(hex(decimal_value)[2:].rjust(2, '0'))
            decimal_value = 0
    return ''.join(hex_string)

def find_similar_images(input_folder, output_folder, threshold = 10):
    # Find and move vaguely similar images from an input folder to an output folder.
    
    # Create the output folder if it doesn't exist.
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # Compute the hash of each image in the input folder.
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.png'):
            image_path = os.path.join(input_folder, filename)
            with Image.open(image_path) as image:
                image_hash = dhash(image)
            # Check if there are other images with similar hashes.
            similar_images = []
            for existing_hash, existing_images in image_hashes.items():
                hamming_distance = sum(c1 != c2 for c1, c2 in zip(image_hash, existing_hash))
                if hamming_distance <= threshold:
                    similar_images.extend(existing_images)
            # Move the image to the output folder if there are similar images.
            if similar_images:
                output_path = os.path.join(output_folder, filename)
                shutil.move(image_path, output_path)
            # Add the image hash to the dictionary.
            image_hashes.setdefault(image_hash, []).append(filename)

# Example usage:

find_similar_images(input_folder, output_folder, threshold)
print('ready processing ', input_folder)

