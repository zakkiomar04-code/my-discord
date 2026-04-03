import discord
from discord import app_commands
from discord.ext import commands
import os
from keep_alive import keep_alive

intents = discord.Intents.default()
client = commands.Bot(command_prefix="!", intents=intents)

@client.tree.command(
    name="hi",
    description="Repeat a message vertically",
)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.describe(message="The text to repeat", times="How many times")
async def hi(interaction: discord.Interaction, message: str, times: int):
    clean_spam = (message + "\n") * times

    if len(clean_spam) > 2000:
        await interaction.response.send_message("That's too much text for one message!", ephemeral=True)
        return

    await interaction.response.send_message(clean_spam)

@client.tree.command(
    name="ban-joke",
    description="Sends a fake Roblox ban message with a reason",
)
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.describe(roblox_user="The Roblox username to fake ban", reason="The reason for the ban")
async def ban_joke(interaction: discord.Interaction, roblox_user: str, reason: str):
    joke_text = f";ban {roblox_user}\n**{roblox_user} got banned from Grow A Garden for {reason}**"
    await interaction.response.send_message(joke_text)

@client.event
async def on_ready():
    await client.tree.sync()
    print(f"Logged in as {client.user}")

keep_alive()
client.run(os.getenv('DISCORD_TOKEN'))
import discord
import os
from discord.ext import commands

# This pulls the token from Koyeb's settings, not from your code!
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ {bot.user} is now online 24/7 on Koyeb!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

bot.run(TOKEN)