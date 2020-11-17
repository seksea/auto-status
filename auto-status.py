import discord
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("token")
parser.add_argument("-t", "--time", help="Time between status change (sec)", type=int)
args = parser.parse_args()

