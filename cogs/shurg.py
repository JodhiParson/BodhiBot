import discord
from discord.ext import commands

class Shrug(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener() #.event
    async def on_ready(self):
        print("Shrug.py is ready!")
    
    @commands.command() #.command
    async def shrug(self, ctx): # note: self goes first before any other parameter
        
        await ctx.send(f"¯\_(ツ)_/¯")
        
async def setup(bot):
    await bot.add_cog(Shrug(bot))