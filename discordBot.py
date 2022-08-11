from turtle import title
import discord, requests, random, pickle
from datetime import datetime

SirBotToken = "Discord Api Token"

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

#discord server id's
servers = ["831609556571258891", "694031693736312932"]

@bot.slash_command(guild_ids = servers, name = "hello", description = "Greet SirBot")
async def hello(ctx):
    await ctx.respond(f"Hello {ctx.author}, My Fellow Sweaty Person")

@bot.slash_command(guild_ids = servers, name = "duck", description = "see duck")
async def duck(ctx):
    response = requests.get("https://random-d.uk/api/v2/random")
    dic = response.json()
    url = dic["url"]

    embed = discord.Embed(title = "Duck")
    embed.set_image(url = url)
    await ctx.respond(embed = embed)

@bot.slash_command(guild_ids = servers, name = "mango", description = "see mango")
async def mango(ctx):
    embed = discord.Embed(title = "Mango")
    dic = {
    1:"https://cdn.discordapp.com/attachments/833072006177488949/1006646185924247703/IMG_3218.JPG", 
    2:"https://cdn.discordapp.com/attachments/833072006177488949/1006646303322820728/lp_image.jpg", 
    3: "https://cdn.discordapp.com/attachments/833072006177488949/1006644237317705860/lp_image.jpg",
    }
    random.seed(datetime.now())
    url = dic[random.randrange(1, len(dic), 1)]
    embed.set_image(url = url)
    await ctx.respond(embed = embed)

@bot.slash_command(guild_ids = servers, name = "kanye", description = "get ye quote")
async def kayne(ctx):
    response = requests.get("https://api.kanye.rest")
    quote = response.json()["quote"]
    await ctx.respond(quote)


@bot.slash_command(guild_ids = servers, name = "bored", description = "you bored, here you go")
async def bored(ctx):
    response = requests.get("http://www.boredapi.com/api/activity/")
    activity = response.json()["activity"]
    await ctx.respond(activity)

@bot.slash_command(guild_ids = servers, name = "wooper", description = "random wooper picture")
async def wooper(ctx):
    fileName = "Disocrd Bot\wooperPNG.pkl"
    openFile = open( fileName, "rb")
    wooperPNGs = pickle.load(openFile)
    openFile.close()
    random.seed(datetime.now())
    img = wooperPNGs[random.randrange(1, len(wooperPNGs), 1)]
    embed = discord.Embed(title = "Wooper")
    embed.set_image(url = img)
    await ctx.respond(embed = embed)


bot.run(SirBotToken)
