import openai
from discord import Intents
import discord
import random
import os

# Discord Token

TOKEN = os.environ.get("DISCORD_TOKEN")
intents = Intents.default()
intents.members = True
client = discord.Client(intents=intents)


# OpenAI api key

openai.api_key = os.environ.get("OPENAI_KEY")
chatbot = openai.Completion()


funny_answers = [
    "🤓 Dame un minutito que me pongo los lentes... ",
    "👀 Leyendo...",
    "✍️ Como no! Resumiendo... ",
    "👾 Dame un toquesito...",
    "🤖 Beep boop! A la orden!",
]


@client.event
async def on_ready():
    """Everytime bot is up and working, this will be printed to stdout"""
    print(f"{client.user} has connected to Discord!")


@client.event
async def on_guild_join(guild):
    channel = guild.text_channels[0]
    await channel.send(
        "👋 Hola! Soy ResumoBot, un bot creado para ayudarte a resumir las conversaciones en canales de texto. ¿Mucho texto? ¿Entraste a un canal y no queres leer todo? ¡Etiquetame y mirá la magia!"
    )


@client.event
async def on_message(message):
    """Action to be performed every time a message is send to a channel in a discord server.
    In this particular case, everytime the bot is mentioned, it'll get the latest 50 messages in desc order,
    and send to OpenAI to be summarized.

    Args:
        message (message): Message object from discord.
    """
    if message.author == client.user:
        return

    if client.user.mentioned_in(message):
        # If and only if the bot is mentioned.
        message_id = message.id
        channel_id = message.channel.id
        channel = client.get_channel(channel_id)

        await message.add_reaction("✈️")
        await channel.send(random.choice(funny_answers))

        channel_history = await get_channel_history(channel)
        ai_response = await get_summary_from_history(chatbot, channel_history)

        await channel.send(ai_response)


async def get_channel_history(channel) -> str:
    """Receives a discord.Channel object, extracting it's message history up to the latest 50 messages.

    Args:
        channel (discord.Channel): Channel object from Discord.

    Returns:
        str: A concatenated string containg the last 50 messages on a specified channel.
    """
    messages = []
    async for message in channel.history(limit=50, oldest_first=False):
        messages.append(message.content)

    # This way we get desc order, older messages last.
    messages.reverse()
    return "\n".join(messages)


async def get_summary_from_history(chatbot, history: str) -> str:
    """Based on a chatbot object using OpenAI token and channel history as string, this generates a summary prompt
    using OpenAI's text-davinci-003 model by default.

    Args:
        chatbot (_type_): OpenAI object initialized with api key.
        history (str): channel's message history in a string format.

    Returns:
        _type_: _description_
    """
    response = chatbot.create(
        engine="text-davinci-003",
        prompt=f"Eres un bot de Discord que se encarga de leer los ultimos mensajes de un canal y dar un resumen. Solo responde con el resumen: {history}",
        max_tokens=500,
    )

    return str(response.choices[0].text)


if __name__ == "__main__":
    client.run(TOKEN)
