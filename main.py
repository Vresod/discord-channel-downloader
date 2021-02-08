import discord
from sys import argv

channel_id = int(argv[1])
path = "." if len(argv) < 3 else argv[2]

client = discord.Client()

disallowed_chars = ["\\","/",":","*","?","<",">","|"," "]

def fix_name(name,replace = "-"):
	for i in ["\\","/",":","*","?","<",">","|"," "]:
		name = name.replace(i,replace)
	return name

with open("tokenfile", "r") as tokenfile:
	token = tokenfile.read()

@client.event
async def on_ready():
	print(f"logged in as {client.user}")
	print(f"https://discord.com/oauth2/authorize?client_id={client.user.id}&permissions=0&scope=bot")

@client.event
async def on_message(message):
	if message.channel.id != channel_id or len(message.attachments) == 0:
		return
	authorname = message.author.display_name
	for char in disallowed_chars:
		authorname = authorname.replace(char,"-")
	if message.content == "":
		filename = f"{path}/{fix_name(message.author.display_name)}.png"
	else:
		filename = f"{path}/{fix_name(message.author.display_name)}-{fix_name(message.content)}.png"
	for attachment in message.attachments:
		await attachment.save(filename)

client.run(token)