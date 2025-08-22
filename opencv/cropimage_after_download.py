import requests
from PIL import Image
import cv2
import numpy as np
import tempfile

# Step 1: Download the image
url = "https://d5klcnu3ka3gl.cloudfront.net/DT/2025/08/22/Chennai/FE/5_20/cf808716_101703735_P_2_mr.jpg"
response = requests.get(url)
response.raise_for_status()

# Step 2: Save to a temporary file
with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
    tmp_file.write(response.content)
    tmp_path = tmp_file.name

# Step 3: Load image with OpenCV
image = cv2.imread(tmp_path)
clone = image.copy()

# Step 4: Select ROI (Region of Interest)
roi = cv2.selectROI("Select Area to Crop", image, showCrosshair=True)
cv2.destroyAllWindows()

# Step 5: Crop and save
x, y, w, h = roi
if w and h:
    cropped = clone[y:y+h, x:x+w]
    save_path = "cropped_image.jpg"
    cv2.imwrite(save_path, cropped)
    print(f"Cropped image saved to {save_path}")
else:
    print("No area selected.")