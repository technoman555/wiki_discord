import logging
import wikipedia as wiki
from discord.ext import commands
import cfg

#logging data
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
#end of logging thank god

def s(search):
   data = wiki.summary(search, sentences= 2)

   return data

#commands
bot = commands.Bot(command_prefix='?')
@bot.event
async def on_ready():
    print("bot online")

@bot.command()
async def w(ctx,search):
    message = await ctx.send("Searching for info on {}".format(search))
    search = s(search)

    await ctx.send("here is what I found for you: {}".format(search))



bot.run(cfg.botid)