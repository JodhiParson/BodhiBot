import discord
from discord.ext import commands

class Changenick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener() #.event
    async def on_ready(self):
        print("Changenick.py is ready!")
    
    @commands.command() #.command
    async def changenick(self, ctx, new_nick): # note: self goes first before any other parameter
        try:
            await ctx.author.edit(nick=new_nick)
            await ctx.send(f"Nickname changed to: {new_nick}")
            
        except discord.Forbidden:
            await ctx.send("I do not have the permissions to change your nickname.")

        
async def setup(bot):
    await bot.add_cog(Changenick(bot))