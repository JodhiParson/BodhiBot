import json
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
    @commands.command()
    async def subscribe(self, ctx, channel_id, *, channel_name):
        # Check if the channel is already subscribed
        with open("youtubedata.json", "r") as f:
            data = json.load(f)

        if channel_id in data:
            await ctx.send("You are already subscribed to this channel.")
        else:
            # You can replace 'YourDiscordChannelID' with the actual channel ID where you want to receive notifications
            self.add_channel(channel_id, channel_name, ctx.channel.id)
            await ctx.send(f"Subscribed to the channel with ID: {channel_id} and name: {channel_name}")

    @commands.command()
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

async def setup(bot):
    await bot.add_cog(SubscriptionCog(bot))
