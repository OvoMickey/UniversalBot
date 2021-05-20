import discord

client = discord.client()

@client.event
async def on_ready():
    print("Bot On")


client.run("TOKEN")
