from PIL import Image, ImageFilter
##
img = Image.open('./source.jpg')
img.thumbnail((400,200)) # this function keeps the aspect ratio even if you give it a value without aspect ratio
img.save('dest.jpg')