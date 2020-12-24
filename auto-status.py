import discord
import json
import datetime
import asyncio

dClient = discord.Client()

# Load config
config = {}
with open("config.json", "r") as f:
    config = json.loads(f.read())

async def statusTask():
    while True:
        for status in config["statuses"]:
            if status["type"] == "game":
                await dClient.change_presence(activity=discord.Game(name=status["name"], start=datetime.datetime.now()-datetime.timedelta(status["duration"]), end=datetime.datetime.now()))
            if status["type"] == "stream":
                await dClient.change_presence(activity=discord.Streaming(name=status["name"], platform="YouTube", url=status["url"]))
            if status["type"] == "competing":
                await dClient.change_presence(activity=discord.Activity(name=status["name"], type=5, details=status["description"]))
            if status["type"] == "watching":
                await dClient.change_presence(activity=discord.Activity(name=status["name"], type=3, details=status["description"]))
            await asyncio.sleep(status["delay"])

@dClient.event
async def on_ready():
    print(f"logged in as {dClient.user} and changing status!")
    dClient.loop.create_task(statusTask())

dClient.run(config["config"]["token"], bot=False)