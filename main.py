import os
import discord
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


# connecting to our bot:
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!poll'):
        # taking all after the word poll:
        question = message.content[len('!poll '):].strip()
        if question:
            poll_message = await message.channel.send(f"Poll: {question}")
            await poll_message.add_reaction('👍')
            await poll_message.add_reaction('👎')
        else:
            await message.channel.send("Zaboravio si da postavis pitanje")

    if "LOL" in message.content:
        await message.channel.send("Ne smijes reci LOL")
        await message.author.kick(reason="Rekao je LOL")

    if message.content == "ping":
        await message.channel.send('pong')
    print(message.content)
    # await message.channel.send('Cao')



client.run(os.getenv("DISCORD_TOKEN"))