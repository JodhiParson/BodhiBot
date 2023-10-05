import discord
from discord.ext import commands

class Embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener() #.event
    async def on_ready(self):
        print("Embed.py is ready!")
    
    @commands.command() #.command
    async def embed(self, ctx): # note: self goes first before any other parameter
        embed_message = discord.Embed(title="Welcome to BodhiBot",description="SUISEX", color=discord.Color.red())
        
        embed_message.set_author(name=f"Requested by @{ctx.author.display_name}", icon_url =ctx.author.avatar)
        embed_message.set_thumbnail(url=ctx.guild.icon)
        embed_message.set_image(url=ctx.guild.icon)
        embed_message.add_field(name="Field name", value="field value", inline=False)
        embed_message.set_footer(text=f"@{ctx.author.display_name}", icon_url=ctx.author.avatar)
        
        await ctx.send(embed = embed_message)
        
async def setup(bot):
    await bot.add_cog(Embed(bot))