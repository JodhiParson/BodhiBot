import discord

from discord.ext import commands

class TextCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener() #.event
    async def on_ready(self):
        print("Text.py is ready!")
        
    @commands.command()
    #shrug
    async def shrug(self, ctx):
        
        await ctx.send(f"¯\_(ツ)_/¯")
        
    @commands.command()
    #tableflip
    async def tableflip(self, ctx):
        
        await ctx.send(f"(╯°□°）╯︵ ┻━┻")
    
    @commands.command() #.command
    async def unflip(self, ctx): # note: self goes first before any other parameter
        
        await ctx.send(f"┬─┬ ノ( ゜-゜ノ)")
        
    
async def setup(bot):
    await bot.add_cog(TextCog(bot))