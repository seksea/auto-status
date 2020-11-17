import discord
import argparse
import asyncio
import datetime

# Parse args
parser = argparse.ArgumentParser()
parser.add_argument("token")
parser.add_argument("-d", "--delay", help="Time between status change (sec)", type=int, default=10)
parser.add_argument("-g", "--game", help="Have a custom game activity", type=int, default=0)
parser.add_argument("-s", "--streaming", action="store_true", help="Have a custom stream activity", default="")
parser.add_argument("-c", "--competing", help="Have a custom 'competing' activity", default="")
args = parser.parse_args()

# Create discord client
dClient = discord.Client()

async def statusTask():
    # Get statuses from file
    with open("statuses.txt", "r") as f:
        statuses = f.readlines()

    print(f"Using statuses {statuses}")
    print(f"Using delay {args.delay}")
    
    # Loop forever and set status
    while True:
        for i in statuses:
            if args.game != 0:
                await dClient.change_presence(activity=discord.Game(name=i[:-1], start=datetime.now()-datetime.timedelta(args.game), end=datetime.noe()))
            elif args.streaming:
                await dClient.change_presence(activity=discord.Streaming(name=i[:-1], platform="YouTube", url="https://www.youtube.com/watch?v=DLzxrzFCyOs"))
            elif args.competing != "":
                await dClient.change_presence(activity=discord.Activity(name=args.competing, type=5, details=i[:-1]))
            await asyncio.sleep(args.delay)

@dClient.event
async def on_ready():
    print(f"logged in as {dClient.user}!")
    dClient.loop.create_task(statusTask())

dClient.run(args.token, bot=False)
