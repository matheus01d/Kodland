import discord
from bot_logic import gen_pass
from bot_logic import flip_coin
# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Fizemos login como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$pass create'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$coin flip'):
        await message.channel.send(flip_coin())
client.run("")
