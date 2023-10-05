import discord
from discord.ext import commands

class Unflip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener() #.event
    async def on_ready(self):
        print("Unflip.py is ready!")
    
    @commands.command() #.command
    async def unflip(self, ctx): # note: self goes first before any other parameter
        
        await ctx.send(f"┬─┬ ノ( ゜-゜ノ)")
        
async def setup(bot):
    await bot.add_cog(Unflip(bot))