import discord
from discord.ext import commands
from youtube_dl import YoutubeDL
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord.utils import get
from discord import FFmpegPCMAudio
import asyncio
import time

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print('다음으로 로그인합니다 : ')
    print(bot.user.name)
    print('connection was succesful')
    await bot.change_presence(status=discord.Status.online, activity=None)

@bot.command()
async def 따라하기(ctx, *, text):
    await ctx.send(embed = discord.Embed(title = '따라하기', description = text, corlor = 0x00ff00))

@bot.command()
async def 접속(ctx):
    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send("**통화방에 접속해주세요!**")

@bot.command()
async def 끊기(ctx):
    try:
        await vc.disconnect()
    except:
        await ctx.send("**봇이 통화방에 없습니다!**")

bot.run('OTU5MzYxNDg0ODQ3MTkwMDI2.YkaxAg.E1AyfsMP6xWOjN9dl5Hyyz1FGaA')