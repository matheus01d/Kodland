import random
import discord
from discord.ext import commands
from bot_logic import flip_coin

intents = discord.Intents.default()
intents.message_content = True

description = "Bot de jogos"
bot = commands.Bot(command_prefix='$', description=description, intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'Fizemos login como {bot.user}')

@bot.hybrid_command()
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Formato tem que ser NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(f"Voce rolou um dado de **{limit} e tirou {result}**")

@bot.hybrid_command()
async def coin_flip(ctx):
    resultado = flip_coin()
    await ctx.send(f"🪙 | Saiu **{resultado}**!")

@bot.hybrid_command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} Entrou {discord.utils.format_dt(member.joined_at)}')


bot.run("TOKEN")


bot.run("TOKEN")
