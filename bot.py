import random
import os
import requests
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

@bot.hybrid_command()
async def meme(ctx):
    await ctx.defer()

    # Pega o caminho exato da pasta onde este script .py está salvo
    pasta_bot = os.path.dirname(os.path.abspath(__file__))
    pasta_images = os.path.join(pasta_bot, "images")
    
    # Colchetes [] criam uma lista para o random.choice funcionar
    meme_random = random.choice(["mem1.jpg", "mem2.jpg", "mem3.jpg"])
    
    # Sem aspas em meme_random para usar o valor sorteado da variável
    caminho_imagem = os.path.join(pasta_images, meme_random)

    with open(caminho_imagem, "rb") as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Uma vez que chamamos o comando duck, o programa chama a função get_duck_image_url '''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("TOKEN")


bot.run("TOKEN")
