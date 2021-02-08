import discord
import requests
from sys import argv

channel_id = argv[1]
path = "." if len(argv) < 3 else argv[2]
print(channel_id,path)

client = discord.Client()

with open("tokenfile", "r") as tokenfile:
	token=tokenfile.read()

@client.event
async def on_message(message):
	if message.channel.id != channel_id:
		return
	
	for x in message.attachments:
		r = requests.get(x.url)
		with open(f"{path}/{x.filename}-{message.author.name}.png", 'wb') as file:
			for chunk in r:
				file.write(chunk)