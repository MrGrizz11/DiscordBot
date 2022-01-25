# IMPORT
import discord # discord
import googletrans # googletrans==4.0.0-rc1
from time import sleep
from dotenv import load_dotenv # python-dotenv
from discord.ext import commands
from const import AVALAIBLE_LANGUAGES, LANGUAGE_VALIDATION, TOKEN

# DEFINE
load_dotenv()
client = discord.Client()
translator = googletrans.Translator()
bot = commands.Bot(command_prefix=">")
translator = googletrans.Translator(service_urls=[
    'translate.google.com',
    'translate.google.co.kr',
])
canCount = 0
isValid = 0
ftext = ''
tradtxt = ''
slang = 'en'
dlang = 'ro'
# DICT FOR "COM" command
botReply = {
    "hello": "Hello there! 👋"
}


# BOT - ACTIVITY/STATUS
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle)


# BOT - ON MESSAGE
@bot.event
async def on_message(message):
    global ftext
    ftext = str(message.content)

    # This is the 'com' command, but is not necessary to write ">com"
    # for userMessage in botReply.keys():
    #     if ftext == userMessage:
    #         await message.channel.send(botReply[userMessage])
            
    await bot.process_commands(message)


# COMMAND - COMMENT
@bot.command()
async def com(comment):
    global botReply
    global ftext

    ftext = ftext[5:]
    for replyTo in botReply.keys():
        if ftext == replyTo:
            await comment.channel.send(botReply[replyTo])


# COMAND - COUNTING
@bot.command()
async def cnt(number):
    global canCount
    global ftext

    strnum = ''
    strnum = ftext[5:]

    if strnum == '1':
        await number.channel.send('1')
    elif strnum == '0':
        await number.channel.send('0')
    else:
        for x in range(1, int(strnum)+1, 1):
            if canCount == 1:
                canCount = 0
                await number.channel.send("```CSS\nCounting stopped\n```")
                break
            else:
                await number.channel.send(x)
            sleep(1)


# COMMAND - STOP COUNTING
@bot.command()
async def stopcnt(stopcounter):
    global canCount
    canCount = 1


# COMAND - CHANGE SOURCE LANGUAGE
@bot.command()
async def sl(sourceLang):
    global slang
    global isValid
    isValid = 0
    slang = ''
    slang = ftext[4:]

    for validLanguage in LANGUAGE_VALIDATION:
        if slang == validLanguage:
            isValid = 1
            break
        
    if isValid == 0:
        await sourceLang.channel.send("```diff\n-Error: Invalid source language, setting default: en```")
        slang = 'en'
    if isValid == 1:
        await sourceLang.channel.send("```ini\n[Source Language: " + slang + "]```")


# COMMAND - CHANGE DESTINATION LANGUAGE
@bot.command()
async def dl(destLang):
    global dlang
    global isValid
    isValid = 0
    dlang = ''
    dlang = ftext[4:]

    for validLanguage in LANGUAGE_VALIDATION:
        if dlang == validLanguage:
            isValid = 1
            break

    if isValid == 0:
        await destLang.channel.send("```diff\n-Error: Invalid destination language, setting default: en```")
        dlang = 'en'
    if isValid == 1:
        await destLang.channel.send("```ini\n[Destination Language: " + dlang + "]```")


# COMMAND - TRANSLATE
@bot.command()
async def t(ctx):
    global ftext, slang, dlang
    ftext = ftext[2:]
    tradtxt = translator.translate(ftext, dest=dlang, src=slang).text
    await ctx.channel.send(tradtxt)


# COMMAND - SHOW AVALAIBLE LANGUAGES
@bot.command()
async def lang(avalaibleLang):
    await avalaibleLang.channel.send("```" + AVALAIBLE_LANGUAGES + "```")


# COMMAND - BOT INFO (HELP)
@bot.command()
async def bothelp(helpcommand):
    await helpcommand.channel.send("""
    ```ini\n
    ---Commands---
    PREFIX >
    
    [Translator]
    1) >t - translates the following text
    ex: >t translate this text
    
    3) >lang - displays all available languages
    
    4) >sl - change the language of the source text
    ex: >sl ru
    ex: >sl russian

    5) >dl - change the destination language
    ex: >dl ro
    ex: >dl romanian

    [Counter]
    1) >cnt (number) - counting up to (number)
    ex: >cnt 69

    2) >stopcnt - to force stop the counter```""")


# BOT.RUN
bot.run(TOKEN)
