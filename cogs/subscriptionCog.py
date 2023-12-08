import json
import re
from discord.ext import commands

class SubscriptionCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("SubscriptionCog.py is ready!")
    
    def remove_channel(self, channel_name):
        # Load existing data from the JSON file
        with open("youtubedata.json", "r") as f:
            data = json.load(f)

        # Check if the channel with the given name exists
        for channel_id, channel_data in list(data.items()):
            if channel_data["channel_name"].lower() == channel_name.lower():
                # Remove the channel using pop
                data.pop(channel_id, None)

                # Save the updated data back to the JSON file
                with open("youtubedata.json", "w") as f:
                    json.dump(data, f)
                
                return True

        return False
    
    @commands.command(aliases=["channellist"])
    async def listchannels(self, ctx):
        # Load data from the JSON file
        with open("youtubedata.json", "r") as f:
            data = json.load(f)

        # Create a formatted message
        message = "List of subscribed channels:\n"
        for channel_id, channel_data in data.items():
            message += f"{channel_data['channel_name']}\n"

        # Send the message to the Discord channel
        await ctx.send(message)
        
    @commands.command(aliases=["follow"])
    async def subscribe(self, ctx, channel_id = None, *, channel_name = None):
        if channel_id is None or channel_name is None:
            await ctx.send("Usage: `=subscribe channel_id channel_name`")
        else: 
        # Check if the channel is already subscribed
            with open("youtubedata.json", "r") as f:
                data = json.load(f) 
               
        # Add the new channel data
            data[channel_id] = {
        "channel_name": channel_name,
        "latest_video_url": "",  # Initialize with empty URL
        "latest_stream_url": "",  # Initialize with empty URL
        "notifying_discord_channel": ctx.channel.id #set to ID of channel where command was used
    }
    # Save the updated data back to youtubedata.json
        with open("youtubedata.json", "w") as f:
            json.dump(data, f, indent=4) 
            

            await ctx.send(f"Subscribed to the channel with ID: {channel_id} and name: {channel_name}")

    @commands.command(aliases=["unfollow"])
    async def unsubscribe(self, ctx, *, channel_name):
        # Attempt to remove the channel
        removed = self.remove_channel(channel_name)
        
        if removed:
            await ctx.send(f"Unsubscribed from: {channel_name}")
        else:
            await ctx.send("Not subscribed to this channel.")

    def add_channel(self, channel_id, channel_name, notifying_discord_channel):
        # Load existing data from the JSON file
        with open("youtubedata.json", "r") as f:
            data = json.load(f)

        # Add the new channel
        data[channel_id] = {
            "channel_name": channel_name,
            "latest_video_url": "",  # You can initialize this with an empty string
            "notifying_discord_channel": notifying_discord_channel
        }

        # Save the updated data back to the JSON file
        with open("youtubedata.json", "w") as f:
            json.dump(data, f)
            
    @commands.command(aliases=["rename_channel"])
    async def rename(self, ctx, channel_name, new_channel_name):
        # Check if the user has permission to manage channels
        if not ctx.author.guild_permissions.manage_channels:
            await ctx.send("You don't have the permission to manage channels.")
            return

        # Load existing data from the JSON file
        with open("youtubedata.json", "r") as f:
            data = json.load(f)

        # Check if the channel with the given name exists
        for channel_id, channel_data in data.items():
            if channel_data["channel_name"].lower() == channel_name.lower():
                # Rename the channel in the JSON data
                channel_data["channel_name"] = new_channel_name

                # Save the updated data back to the JSON file
                with open("youtubedata.json", "w") as f:
                    json.dump(data, f)

                await ctx.send(f"Channel '{channel_name}' renamed to '{new_channel_name}'.")
                return

        await ctx.send(f"Channel '{channel_name}' not found in your subscriptions.")
async def setup(bot):
    await bot.add_cog(SubscriptionCog(bot))
