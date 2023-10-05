import discord
from discord.ext import commands
import random

class Fortune(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener() #.event
    async def on_ready(self):
        print("Fortune.py is ready!")
    
    @commands.command(aliases = ["8ball", "eightball", "eight ball", "8 ball"]) #.command
    async def fortune(self, ctx, *, question):
        with open("responses.txt","r") as f:
            random_responses = f.readlines()
            response = random.choice(random_responses)
            await ctx.send(response)
            
    # Define an error handler for the MissingRequiredArgument exception; doesn't work right now
    @fortune.error
    async def fortune_error(self, ctx, error):
     if isinstance(error, commands.MissingRequiredArgument):
         await ctx.send("PLEASE ASK BODHI A QUESTION FIRST!")

    

async def setup(bot):
    await bot.add_cog(Fortune(bot))