import pytesseract
from PIL import Image, ImageFilter
from pathlib import Path
from natsort import natsorted


f = open("output.txt", "w+") # create empty output file
images_folder = Path('data').glob('*.png') # get all images in the data folder
images_folder = natsorted(images_folder, key=str) # sort images
tesseract_config = '--psm 6 digits -c tessedit_char_whitelist=0123456789.-' # configure tesseract to focus on digits

for img in images_folder:
    image = Image.open(img)
    image = image.filter(ImageFilter.SHARPEN)
    text = pytesseract.image_to_string(image, config=tesseract_config)
    f.write(text)
    print(f'Extracted digit from {img}')

f.close()