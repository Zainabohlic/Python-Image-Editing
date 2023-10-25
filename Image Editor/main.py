from PIL import Image, ImageEnhance, ImageFilter
import os

path = "./img" # folder for unedited images
pathOut = "/editedImg" # folder for edited images

for filename in os.listdir(path):
    # each file image in the folder accessing it with path
    img = Image.open(f"{path}/{filename}")

    # adding smooth effect
    edit = img.filter(ImageFilter.SMOOTH).convert('L').rotate(-360)

    # contrast
    factor = 0.8
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)


    new_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{new_name}_edited.jpg')