import discord
from discord.ext import commands
import json
import requests
import os
from dotenv import load_dotenv
load_dotenv()


class Embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener() #.event
    async def on_ready(self):
        print("Embed.py is ready!")
    
    @commands.command(aliases=["channels","list"]) #.command
    async def embed(self, ctx): # note: self goes first before any other parameter
        # Load data from the JSON file
        with open("youtubedata.json", "r") as f:
            data = json.load(f)
            
        embed_message = discord.Embed(title="Subscribed Channels", color=discord.Color.red())
        
        embed_message.set_author(name=f"Requested by @{ctx.author.display_name}", icon_url =ctx.author.avatar)
        embed_message.set_thumbnail(url=ctx.author.avatar)
        #embed_message.set_image(url=ctx.guild.icon)
        for channel_id, channel_data in data.items():
            profile_picture_url = self.get_channel_profile_picture(channel_id)
            embed_message.add_field(
                name=channel_data['channel_name'],
                value=f"Channel ID: {channel_id}",
                inline=False
            )
        embed_message.set_thumbnail(url=profile_picture_url)
        embed_message.set_footer(text=f"@{ctx.author.display_name}", icon_url=ctx.author.avatar)
        
        await ctx.send(embed = embed_message)
        
    def get_channel_profile_picture(self, channel_id):
        # Use your YouTube Data API key here
        api_key = os.getenv('YOUTUBE_API_KEY')

        # Make a request to the YouTube Data API
        url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet&id={channel_id}&key={api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if 'items' in data and len(data['items']) > 0:
                return data['items'][0]['snippet']['thumbnails']['default']['url']
        return "No Image Found"  # Default image if the profile picture is not available
        
    @commands.command()
    async def info(self, ctx):
        await ctx.send("hi")
            
async def setup(bot):
    await bot.add_cog(Embed(bot))