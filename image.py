from ctypes import sizeof
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open('images/3C7E8577-1DD8-B71B-0B5ABB3F175DDD81.jpg')
d1 = ImageDraw.Draw(img)

# font = ImageFont.load_default()
font = ImageFont.truetype("GidoleFont/Gidole-Regular.ttf", 100)

d1.text((100, 0), "Hello, TutorialsPoint!", fill=(255, 255, 255), font=font)
img.resize((600,448))
img.save("images/image_text.jpg")