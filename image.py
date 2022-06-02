from ctypes import sizeof
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def convert_image(description):
    img = Image.open('images/image.jpg')
    img = img.resize((600,448))

    d1 = ImageDraw.Draw(img)
    font = ImageFont.truetype("GidoleFont/Gidole-Regular.ttf", 25)
    d1.text((0, 0), description, fill=(255, 255, 255), font=font, stroke_width=2, stroke_fill=(0, 0, 0))
    img.save("images/image_text.jpg")