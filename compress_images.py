import os
import sys
# pip install pillow
# PIL - Python Image Library
from PIL import Image

img_source_path = "/home/vinoth/Pictures/05-08-2023-Gettogether/"
img_name = "IMG_1076.JPG"
source_img_full = f"{img_source_path}{img_name}"

#Check if the image source path is valid
if not os.path.exists(img_source_path):
  sys.exit("Image source path {img_source_path} not found")

# Check if the source image exists
if not os.path.exists(source_img_full):
  sys.exit("Source image doesn't exist")

compressed_file_path = f"{img_source_path}compressed/"
#Create the dir if it doesn't exist already
if not os.path.exists(compressed_file_path):
  os.mkdir(compressed_file_path)

compressed_img_name = f"{img_name.split('.')[0]}_compressed.{img_name.split('.')[1]}"
print(f"Compressed file name: {compressed_file_path}{compressed_img_name}")
compressed_img_name_full = f"{compressed_file_path}{compressed_img_name}"

img = Image.open(source_img_full)

original_width, original_height = img.size
print(f"Original Image Size: W: {original_width}, H: {original_height}")
new_size_ratio = 0.5
new_width = int(original_width * new_size_ratio)
new_height = int(original_height * new_size_ratio)
resized_image = img.resize((new_width, new_height))

resized_image.save(compressed_img_name_full, optimize=True, quality=100)
