import discord
from discord.ext import commands

class TableFlip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener() #.event
    async def on_ready(self):
        print("TableFlip.py is ready!")
    
    @commands.command() #.command
    async def tableflip(self, ctx): # note: self goes first before any other parameter
        
        await ctx.send(f"(╯°□°）╯︵ ┻━┻")
        
async def setup(bot):
    await bot.add_cog(TableFlip(bot))