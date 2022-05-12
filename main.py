# from keep_alive import keep_alive
import discord
from discord.ext import commands
from discord.ext.audiorec import NativeVoiceClient
from discord_ui import Components, UI, SelectMenu, SelectOption, Button
import random
import os
import asyncio
from funcs import randomCountry, randomPicOfCountry, randomCountries
from appwriteFuncs import checkExistence, makeUser, updateScore
import creds

intents = discord.Intents().all()
client = commands.Bot(command_prefix="t ", intents=intents)
client.remove_command('help')
ui = UI(client)

ListOfCommands = ['t country']


@client.event
async def on_ready():
    print('im ready')


@client.event
async def on_message(message):
    # print(message.content)
    if message.content in ListOfCommands:
        await asyncio.sleep(1.5)
        await message.add_reaction('✅')
    await client.process_commands(message)


@client.command()
async def test(ctx):
    await ctx.send('yes')


@client.command()
async def create(ctx):
    if checkExistence(str(ctx.author.id)):
        await ctx.send('you already have an account!')
    else:
        makeUser(ctx.author.id, ctx.author.display_name)
        await ctx.send('made account!')


@ client.command()
async def country(ctx):
    if checkExistence(ctx.author.id):
        correct_option = 'z'
        countryChosen = randomCountry()
        filename = randomPicOfCountry(countryChosen)
        country_options = randomCountries(3)
        country_options.append(countryChosen)
        # print(countryChosen)
        options_letters = ['a', 'b', 'c', 'd']
        emojis = ["🇦", "🇧", "🇨", "🇩"]
        options = list()
        random.shuffle(country_options)
        pointer = 0
        for country in country_options:
            if country == countryChosen:
                correct_option = options_letters[pointer]
            options.append(
                f':regional_indicator_{options_letters[pointer]}: {country}')
            pointer += 1
        embeded = discord.Embed(title="Guess the country",
                                description='Guess the country the image is related to!\n**YOU HAVE ONLY 5 SECONDS TO ANSWER, SO BE QUICK!!**', color=0x2ecc71)
        embeded.set_image(url=f'attachment://{filename[0]}.jpg')
        file = discord.File(
            f"{filename[0]}.jpg", filename=f"{filename[0]}.png")
        embeded.set_image(url=f"attachment://{filename[0]}.png")
        embeded.add_field(name="Your Options",
                          value='\n'.join(options), inline=False)
        message = await ctx.send(file=file, embed=embeded)
        for emoji in emojis:
            await message.add_reaction(emoji)

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == emojis[options_letters.index(correct_option)]

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=5.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send(f'incorrect response! the answer was **{countryChosen}**')
        else:
            updateScore(ctx.author.id, 100)
            await ctx.send('correct answer! you have been given 100 points!')
    else:
        await ctx.send('you dont have an account yet!, use **!create** to make an account!')
    # os.remove(f'{filename[0]}.jpg')
    # https://discordpy.readthedocs.io/en/latest/ext/commands/api.html?highlight=wait_for#discord.ext.commands.Bot.wait_for
    # work on reaction like system to get option


client.run(creds.bot_key)

# imolemt method for quix thingy
