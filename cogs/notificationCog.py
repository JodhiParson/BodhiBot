import json
import discord
from discord.ext import commands

class NotificationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("NotificationCog.py is ready!")

    @commands.command(aliases=["set_channel","setchannel","channelset","channel_set"])
    async def set_notification_channel(self, ctx, *, channel_name=None):
        if channel_name is None:
            # If no channel name is provided, set the notifying Discord channel to the current channel
            channel_id = ctx.channel.id
        else:
            # Remove leading and trailing whitespaces and check if the name starts and ends with quotes
            if channel_name.startswith('"') and channel_name.endswith('"'):
                # Remove the quotes and leading/trailing whitespaces
                channel_name = channel_name[1:-1].strip()

            # Find the channel by name
            channel = discord.utils.get(ctx.guild.channels, name=channel_name)

            if channel is None:
                await ctx.send(f"Channel '{channel_name}' not found.")
                return

            channel_id = channel.id

        # Load existing data from the JSON file
        with open("youtubedata.json", "r") as f:
            data = json.load(f)

        # Update the notifying Discord channel for all subscribed channels in the current guild
        for channel_data in data.values():
            if channel_data["notifying_discord_channel"] != channel_id:
                channel_data["notifying_discord_channel"] = channel_id

        # Save the updated data back to the JSON file
        with open("youtubedata.json", "w") as f:
            json.dump(data, f)

        await ctx.send(f"Notifying Discord channel set to {ctx.channel.mention}")

async def setup(bot):
    await bot.add_cog(NotificationCog(bot))
