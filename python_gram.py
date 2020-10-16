import argparse, os, sys, random, creds, emoji
from pycam import capture_plant
from events import events
from datetime import date
from caption_maker import weather_caption, feeling
from instabot import Bot

plant_emojis = [":four_leaf_clover:", ":deciduous_tree:", ":herb:", ":cactus:", ":seedling:", ":evergreen_tree:"]

sys.path.append(os.path.join(sys.path[0], "../"))

event_text = str(f"{events()}\n") if events != "" else event_text = events()

caption = f"{date.today()}  {emoji.emojize(random.choice(plant_emojis))}\n{event_text}{weather_caption()}°C i am {feeling()}!\n\n\n\n#plants #nature #bot"

bot = Bot()
bot.login(username=creds.u, password=creds.p)
capture_plant()
bot.upload_photo("image.jpg", caption)

print(caption)
