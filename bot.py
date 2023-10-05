# bot.py
import os
import discord
import json
import requests
import re
import random
import asyncio

from discord.ext import commands, tasks

from dotenv import load_dotenv


intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix="=",intents=intents)

#ONREADY
@bot.event
async def on_ready():
    print("BODHI BOT IS READY FOR USE")
    print("-----------------------")
    """
        Setup the game status task of the bot.
        """
    change_status.start()
    checkforvideos.start()

#note: 'async' functions ALWAYS need an 'await' somewhere in the function
async def load():
  for filename in os.listdir("./cogs"):
      if filename.endswith(".py"):
        await bot.load_extension(f"cogs.{filename[:-3 ]}") #splicing (takes the last 3 characters of the filename) Ex: myCog.py -> myCog
        print(f"{filename[:-3]} is loaded!")

async def main():
  async with bot:
    await load()
    await bot.start('YOUR_TOKEN_HERE')

@tasks.loop(seconds=86400)
async def change_status():
  statuses = ["Sui-chan💕☄️", "Ogayu🍙", "SHUBA🦢","Doggo🐶","POL🤡","SODA-CHAN🐻","HAROBO🤖","WAMY🍶❄️","PEKO🐰","BAU BAU🐾","BIBOO🗿","BO☔","FAUNA🌿 UUUUU🥺"]
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=random.choice(statuses)))
    

@bot.event #HELLO WORLD
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("hi"):
        await message.channel.send("Hello World!")
    await bot.process_commands(message) #process messages

#checking for vidoes every 30 seconds
#you can check for vidoes every 10 seconds also but i would prefer to keep 30 seconds
@tasks.loop(seconds=30)
async def checkforvideos():
  with open("youtubedata.json", "r") as f:
    data=json.load(f) # loads the data in the json
  
  #printing here to show
  #print("Now Checking!")

  #checking for all the channels in youtubedata.json file
  for youtube_channel in data:
    #print(f"Now Checking For {data[youtube_channel]['channel_name']}")
    #getting youtube channel's url
    channel = f"https://www.youtube.com/channel/{youtube_channel}"

    #getting html of the /videos page
    videohtml = requests.get(channel+"/videos").text

    #getting the latest video's url
    #put this line in try and except block cause it can give error some time if no video is uploaded on the channel
    try:
       latest_video_url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', videohtml).group()
    except:
        continue
    #checking if url in youtubedata.json file is not equals to latest_video_url
    if not str(data[youtube_channel]["latest_video_url"]) == latest_video_url:
        print("a video has been uploaded!")
      #changing the latest_video_url
        data[str(youtube_channel)]['latest_video_url'] = latest_video_url

      #dumping the data
        with open("youtubedata.json", "w") as f:
           json.dump(data, f)

      #getting the channel to send the message
        discord_channel_id = data[str(youtube_channel)]['notifying_discord_channel']
        discord_channel = bot.get_channel(int(discord_channel_id))

      #sending the msg in discord channel
      #you can mention any role like this if you want
        msg = f"@everyone {data[str(youtube_channel)]['channel_name']} Just Uploaded A Video or they are Live Go Check It Out: {latest_video_url}"
      #if you'll send the url discord will automaitacly create embed for it
      #if you don't want to send embed for it then do <{latest_video_url}>

        await discord_channel.send(msg)





#run client
asyncio.run(main())
