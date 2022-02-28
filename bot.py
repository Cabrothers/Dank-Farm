
import discord, os, asyncio

from discord.ext import commands

from colorama import Fore, Style

token = "Enter Token Here"

#Bot prefix, like ?help 

prefix = "."

def endSong(guild, path):

    os.remove(path)

#Clear Command

def Clear():

    os.system('clear')

#Colors

def RandomColor():

    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))

    return randcolor

def RandString():

    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))

#Prefix

client = discord.Client()

client = commands.Bot(command_prefix=prefix,self_bot=True)

#Farm

@client.command(name='dank-farm', aliases=['dankfarm', 'dm'])

async def _fish_dank(ctx): # b'\xfc'

    await ctx.message.delete()

    count = 0

    while True:

        try:

            count += 1

            await ctx.send('pls fish')

            await ctx.send('pls hunt')

            await ctx.send('pls dig')

            await ctx.send('pls beg')

            print(f'{Fore.BLUE}[AUTO-FARM] {Fore.GREEN}Farm number: {count} sent'+Fore.RESET)

            await asyncio.sleep(26)

        except Exception as e:

            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

           

#onReady

@client.event

async def on_ready():

	print(f"You are Online :)")

client.run(token,bot=False)
