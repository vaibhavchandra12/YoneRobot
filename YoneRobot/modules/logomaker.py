from YoneRobot.events import register
from YoneRobot import OWNER_ID
from YoneRobot import telethn as tbot
import os 
import io
import requests
import shutil 
import random
import re
import glob
import time
from PIL import Image, ImageDraw, ImageFont

LOGO_LINKS            = ["https://telegra.ph/file/74807bfbc85057899ea8d.png",
                         "https://telegra.ph/file/4606e5c76a4a6c893a721.png",
                         "https://telegra.ph/file/1daa50b9d3e26a5509cc2.png",
                         "https://telegra.ph/file/22a5d3621aba0b370d0b6.png",
                         "https://telegra.ph/file/ae31845d1df2c4a84915b.png",
                         "https://telegra.ph/file/ae2b809c8d11e7fa4121d.png",
                         "https://telegra.ph/file/ccb7f3113994d5d2b26f6.png",
                         "https://telegra.ph/file/5e53f0257ff12a7b0737a.png",
                         "https://telegra.ph/file/11585459a3950de7f307c.png",
                         "https://telegra.ph/file/d8d2db623223dee65963e.png",
                         "https://telegra.ph/file/9e4bef8ae0725d6b62108.png",
                         "https://telegra.ph/file/8bd2b561b4c1f7164f934.png",,
                         "https://telegra.ph/file/5935275d3ee09bc5a47b8.png",
                         "https://telegra.ph/file/b29d8956ae249773b0ec7.png"
                         ]

@register(pattern="^/logo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:

  if not quew:
     await event.reply('Please Give A Text For Your Logo.')
     return
 pesan = await event.reply('Asking X-MEN for BG..Done')
 try:
    text = event.pattern_match.group(1)
    randc = random.choice(LOGO_LINKS)
    img = Image.open(io.BytesIO(requests.get(randc).content))
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "black"
    shadowcolor = "blue"
    fnt = glob.glob("./YoneRobot/resources/**")
    randf = random.choice(fnt)
    font = ImageFont.truetype(randf, 120)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y = ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="white", stroke_width=1, stroke_fill="black")
    fname = "livvy.png"
    img.save(fname, "png")
    await tbot.send_file(event.chat_id, file=fname, caption = f"Made By @MissLivvyBot, Join @RhythmOff")         
    await pesan.delete()
    if os.path.exists(fname):
            os.remove(fname)
 except Exception as e:
    await event.reply(f'Error, Report @RhythmOff, {e}')


@register(pattern="^/blogo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:
     
    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Asking X-MEN for BG..Done')
 try:
    text = event.pattern_match.group(1)
    img = Image.open('./YoneRobot/resources/blackbg.jpg')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("./YoneRobot/resources/Chopsic.otf", 330)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="black", stroke_width=25, stroke_fill="yellow")
    fname2 = "blivvy.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By @MissLivvyBot, Join @RhythmOff")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error, Report @RhythmOff, {e}')



   
@register(pattern="^/wlogo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:
     
    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Asking X-MEN for BG..Done')
 try:
    text = event.pattern_match.group(1)
    img = Image.open('./YoneRobot/resources/blackbg.jpg')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "white"
    shadowcolor = "blue"
    font = ImageFont.truetype("./YoneRobot/resources/Maghrib.ttf", 1000)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="white", stroke_width=0, stroke_fill="white")
    fname2 = "wlivvy.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By @MissLivvyBot, Join @RhythmOff")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error, Report @RhythmOff, {e}')

file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")


__help__ = """
 ❍ /logo text :  Create your logo with your name with random bg
 ❍ /wlogo text :  Create your logo with your name with black bg
 ❍ /blogo text :  Create your logo with your name with random bg
 """
__mod_name__ = "Logo"
