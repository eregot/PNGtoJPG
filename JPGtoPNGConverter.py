import sys
import os
from PIL import Image

# grab first and second arguments
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if output folder exists, create it if not
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through the pokedex
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}/{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}/{clean_name}.png', 'png')
    print('all done!')