from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
# pring(dir(img))  - this helps to get all the methods e.g filter save that can be used with img
# filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img = img.convert('L')


filtered_img.save("grey.png", "png")
