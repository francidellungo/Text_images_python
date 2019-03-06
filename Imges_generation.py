from PIL import Image, ImageDraw, ImageFont
import textwrap
from win32api import GetSystemMetrics

print("Width =", GetSystemMetrics(0))
print("Height =", GetSystemMetrics(1))
image_width = GetSystemMetrics(0)
image_height = GetSystemMetrics(1)

"""-----------------
PARAMETERS:"""

space_btw_lines = int(image_height/7)
font_size = 100
margin = int(image_width/20)
max_text_length = image_height - int(margin/2) -100

print('space btw lines: '+str(space_btw_lines)+', font size: '+str(font_size)+', margin: '+str(margin)+' , max text length: '+str(max_text_length))
"""-------------------"""
imgs_path = '.\\imgs\\'
#img = Image.new('RGB', (2700, 1300), color = 'white')
images = []

img = Image.new('RGB', (image_width, image_height), color = 'white')
images.append(img)
my_font = ImageFont.truetype('arial.ttf', font_size)

d = ImageDraw.Draw(images[0])
f = open("PromessiSposi.txt", "r")
#f = open("DivinaCommedia.txt", "r")

text = f.read()
#d.text(xy=(10,10), text=text, fill='black', font=my_font)

lines = textwrap.wrap(text, width = int(image_width/55)) #This width value needs to be set automatically
y_text = 0
num_page = 0
for num_line in range(len(lines)):
    #print(num_line)
    if y_text >= max_text_length:
        y_text = 0
        print('fine pagina', num_page)
        # images[num_page].show('PHOTO_'+str(num_page)+'.png')
        images[num_page].save(imgs_path+'PHOTO_'+str(num_page)+'.png')
        num_page = num_page + 1
        img = Image.new('RGB', (image_width,image_height), color = 'white')
        images.append(img)
        d = ImageDraw.Draw(images[num_page])
    elif lines[num_line] == lines[-1]:
        print('fine testo')
        d.text((margin, y_text), lines[num_line], font = my_font, fill = 'black')
        # images[num_page].show('PHOTO_'+str(num_page)+'.png')
        images[num_page].save(imgs_path+'PHOTO_'+str(num_page)+'.png')
        break
    else:
        d.text((margin, y_text), lines[num_line], font = my_font, fill = 'black')
        y_text += space_btw_lines




