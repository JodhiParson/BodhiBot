import discord
from discord.ext import commands, tasks
from googleapiclient.discovery import build
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')


class Streamer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener() #.event
    async def on_ready(self):
        print("Streamer.py is ready!")

    @tasks.loop(seconds=30)
    async def checkforstreams():
        with open("youtubedata.json", "r") as f:
            data=json.load(f) # loads the data in the json
    
async def setup(bot):
    await bot.add_cog(Streamer(bot))