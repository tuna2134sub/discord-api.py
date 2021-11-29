from discord_api import Client, Command, Embed, InteractionTypeCommand
import asyncio
from os import getenv
import json
from asyncio import sleep

client = Client(log = False)

client.add_command(Command("test4", "This is for test."))

@client.event
async def on_ready():
    print("起動")
    await sleep(3)
    channel = client.get_channel(910909233023840306)
    await channel.send("起動", embeds = [Embed(title = "title", description = "description")])

@client.event
async def on_interaction(i):
    print(i.author.id)
    if i.type == InteractionTypeCommand:
        await i.send(i.guild.text_channels[0].id, True)

@client.event
async def on_gateway_response(data):
    with open(f"{data['t']}.json", "w") as f:
        json.dump(data, f, indent = 4)

client.run(getenv("token"))