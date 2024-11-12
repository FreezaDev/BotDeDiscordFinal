import discord
import random
from discord.ext import commands
import asyncio
import os
import requests

timer = 0.0
running = False
eightballmsg = ["Si, definitivamente", "SI 🔥", "Probablemente", "Quien sabe?",
"No lo debo decir", "Nah", "NO 🔥", "Definitivamente no", "Consulta mas tarde"]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='=', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def dado10(ctx):
    await ctx.send(random.randint(1,10))

@bot.command()
async def dado6(ctx):
    await ctx.send(random.randint(1,6))

@bot.command()
async def bola8(ctx):
    await ctx.send(random.choice(eightballmsg))

@bot.command()
async def tempo(ctx):
    global running
    global timer
    if running:
        running = False
        await ctx.send(f"Tardaste {int(timer)} segundos")
    else:
        running = True
        timer = 0.0
        await ctx.send("Has empezado el temporizador, llama el comando nuevamente para detenerlo")

    while running:
        await asyncio.sleep(0.1)
        timer += 0.1

def dogg():    
    url = "https://random.dog/woof.json"
    res = requests.get(url)
    data = res.json()
    return data["url"]


@bot.command()
async def perro(ctx):
    image_url = dogg()
    await ctx.send(image_url)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
    
@bot.command('duck')
async def pato(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def contaminacion(ctx):
    await ctx.send(f"La contaminacion es un problema muy grande en el mundo, tambien es la causa de el calentamiento global")
    await ctx.send("Quieres saber sobre la regla de las tres erres? (si/no)")

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ["Sí", "sí", "Si", "si", "No", "no"]
    response = await bot.wait_for('message', check=check)
    if response:
        if response.content in ["Sí", "sí", "Si", "si"]:
            await ctx.send("Las tres erres son \"Reducir, Reutilizar y Reciclar\"")
            await ctx.send("Reducir: Puedes aportar reduciendo la electricidad o el agua que gastas en el dia a dia para conservar recursos")
            await ctx.send("Reutilizar: Reutiliza los objetos que puedes darle una segunda vida util, como hacer papel mache con hojas de periodico")
            await ctx.send("Reciclar: Deposita basura en contenedores de reciclaje para que puedan volver a ser usados para la creacion de materiales (Por ejemplo, botellas de vidrio)")  
        else:
            await ctx.send("Si algun dia quieres saber, me tienes aqui")
    else:
        await ctx.send("QUE TE DIJE SI O NO")
    await ctx.send("Te gustaria, ademas, saber la definicion de contaminacion? (si/no)")
    response1 = await bot.wait_for('message', check=check)
    if response1:
        if response1.content in ["Sí", "sí", "Si", "si"]:
            await ctx.send("A lo que se considera \"contaminacion\" es la presencia de un elemento indeseable que arruina un entorno") 
        else:
            await ctx.send("Tienes google de todos modos")
    else:
        await ctx.send("QUE TE DIJE SI O NO")



bot.run("Token")












