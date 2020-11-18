import discord
import argparse
import asyncio
import datetime
import random

# Parse args
parser = argparse.ArgumentParser()
parser.add_argument("token")
parser.add_argument("-d", "--delay", help="Time between status change (sec)", type=int, default=10)
parser.add_argument("-g", "--game", help="Have a custom game activity", type=int, default=0)
parser.add_argument("-s", "--streaming", action="store_true", help="Have a custom rickroll stream activity")
parser.add_argument("-c", "--competing", help="Have a custom 'competing in' activity", default="")
parser.add_argument("-w", "--watching", help="Have a custom 'watching' activity", default="")
parser.add_argument("-r", "--random", action="store_true", help="Pick a random status", default="")
args = parser.parse_args()

# Create discord client
dClient = discord.Client()

async def statusTask():
    # Get statuses from file
    with open("statuses.txt", "r") as f:
        activities = f.readlines()

    print(f"Using activities {activities}")
    print(f"Using delay {args.delay}")

    # Loop forever and set status
    while True:
        for activity in activities:
            if args.random:
                activity = random.choice(activities)
            if activity.endswith("\n"):
                activity = activity[:-1]
            if args.game != 0:
                await dClient.change_presence(activity=discord.Game(name=activity, start=datetime.datetime.now()-datetime.timedelta(args.game), end=datetime.datetime.now()))
            elif args.streaming:
                await dClient.change_presence(activity=discord.Streaming(name=activity, platform="YouTube", url="https://www.youtube.com/watch?v=DLzxrzFCyOs"))
            elif args.competing != "":
                await dClient.change_presence(activity=discord.Activity(name=args.competing, type=5, details=activity))
            elif args.watching != "":
                await dClient.change_presence(activity=discord.Activity(name=activity, type=3, details=args.watching))
            await asyncio.sleep(args.delay)

@dClient.event
async def on_ready():
    print(f"logged in as {dClient.user}!")
    dClient.loop.create_task(statusTask())

dClient.run(args.token, bot=False)
