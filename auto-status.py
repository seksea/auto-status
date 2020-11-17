import discord
import argparse

# Parse args
parser = argparse.ArgumentParser()
parser.add_argument("token")
parser.add_argument("-t", "--time", help="Time between status change (sec)", type=int)
args = parser.parse_args()

# Create discord client
dClient = discord.Client()

@dClient.event
async def on_ready():
    print(f"logged in as {dClient.user}!")
    

dClient.run(args.token, bot=False)