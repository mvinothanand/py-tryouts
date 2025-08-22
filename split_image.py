from PIL import Image
import os

def split_image(image_path, output_dir, split_size):
    """
    Splits an image into multiple parts based on the given split size.

    :param image_path: Path to the input image file.
    :param output_dir: Directory to save the split images.
    :param split_size: Tuple (split_width, split_height) specifying the size of each split in pixels.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        with Image.open(image_path) as img:
            img_width, img_height = img.size
            split_width, split_height = split_size

            rows = img_height // split_height
            cols = img_width // split_width

            for row in range(rows):
                for col in range(cols):
                    left = col * split_width
                    upper = row * split_height
                    right = min(left + split_width, img_width)
                    lower = min(upper + split_height, img_height)

                    cropped_img = img.crop((left, upper, right, lower))
                    output_file = os.path.join(output_dir, f"tile_{row}_{col}.png")
                    cropped_img.save(output_file)

            print(f"Image successfully split into {rows * cols} parts.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    input_image = "/mnt/c/Users/Vinoth Masilamani/Pictures/temp/202507/composite-kovalam-20250713.jpg"  # Replace with your image file path
    output_directory = "/mnt/c/Users/Vinoth Masilamani/Pictures/temp/202507/composite-split"
    split_size = (800, 1000)  

    split_image(input_image, output_directory, split_size)
