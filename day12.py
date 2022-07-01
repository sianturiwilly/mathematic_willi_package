# Bootcamp Python Pertemuan Ke-12
# Tanggal: 6 April 2022

# Membuka file gambar.
# nike.show()

# print(nike.size)
# print(nike.format)
# print(nike.mode)

# blurr = nike.filter(ImageFilter.BLUR)
# blurr.show()
# blurr.save("nikeardilla_blurr.jpg")

# blurr = nike.filter(ImageFilter.SMOOTH)
# blurr.save("nikeardilla_smooth.jpg")

# blurr = nike.filter(ImageFilter.EMBOSS)
# blurr.save("nikeardilla_emnboss.jpg")

# blurr = nike.filter(ImageFilter.SHARPEN)
# blurr.save("nikeardilla_sharpen.jpg")

# gs = nike.convert("L")
# gs.save("nikeardilla_red.jpg")

# cropped = nike.crop(100, 100, 350, 350))
# cropped.save('nikeardilla_cropped.jpg')

# crop = nike.crop((10, 10, 200, 200))
# crop.show("nikeardilla_crop.jpg")

# rotate = nike.rotate(90)
# rotate.show("nikeardilla_90.jpg")

from PIL import Image, ImageDraw, ImageFont

nike = Image.open("nikeardilla.jpg")

idraw = ImageDraw.Draw(nike)
text = "Copyright 2022"

font = ImageFont.truetype("arial.ttf", size=15)

idraw.text((400, 10), text, font=font, fill=(0,0,0))
nike.save("nikeardilla_watermark.jpg")