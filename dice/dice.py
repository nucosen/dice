from typing import List
import discord
import re
from random import randint, choice
import os
from logging import INFO, basicConfig, getLogger
from json import load
from decouple import UndefinedValueError, AutoConfig
from discord import client
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from dice.text import *


# FIXME ロギングレベル変更中 <<< REMOVE BEFORE DEPLOY >>>
basicConfig(
    format='{asctime} [{levelname:4}] {message}',
    style='{',
    # level=INFO
)


def run():
    logger = getLogger(__name__)
    logger.info("Starting Dice-KUN...")

    client = commands.Bot(command_prefix='@', intents=discord.Intents.all())
    slash_client = SlashCommand(client, sync_commands=True)

    try:
        config = AutoConfig(search_path=os.getcwd())
        logger.info("CWD is {0}".format(os.getcwd()))
        TOKEN = config("DISCORD_DICE_TOKEN")
    except UndefinedValueError:
        logger.critical("Discord token is NOT FOUND.")
        exit()

    try:
        servers: List = config("DISCORD_DICE_SERVERS").split(",")
    except UndefinedValueError:
        logger.warn("No server is allowed to run slash command.")
        servers = []
    else:
        logger.info(
            "{0} server(s) is/are allowed to run slash command.".format(len(servers))
        )
        servers = list(map(int, servers))

        logger.info("--- Arrowed servers list begin ---")
        for server in servers:
            logger.info(str(server))
        logger.info("--- Arrowed servers list end ---")

    @client.event
    async def on_message(message):

        if isinstance(message, discord.Message):
            if message.author.bot:
                return

        if client.user in message.mentions:
            await message.add_reaction(choice(emoji_list))
            embed = discord.Embed(
                title="「ダイス君 v4.1.1」で出来ること",
                description=Guide,
                color=discord.Colour.blue()
            )
            logger.info("Dice-kun is active !")
            await message.channel.send(embed=embed)
            return

        if match := re.search("([0-9]{1,4})d([0-9]{1,4})!", message.content):
            await message.add_reaction("\N{GAME DIE}")
            resultMessage = message.content
            rolledDiceList = []
            while True:
                count = int(match.groups()[0])
                randmax = int(match.groups()[1])
                result = 0
                if count != 0 and randmax != 0:
                    for _ in range(count):
                        result += randint(1, randmax)
                resultMessage = resultMessage.replace(
                    match.group(), f" `{result}` ", 1
                )
                rolledDiceList.append(match.group()[:-1] + f"：**{result}**")
                if not (match := re.search("([0-9]{1,4})d([0-9]{1,4})!", resultMessage)):
                    break
            embed = discord.Embed(
                title="Dice Roll",
                description=resultMessage + "\n" + "\n".join(rolledDiceList),
                color=discord.Color.green()
            )
            await message.channel.send(reference=message, mention_author=True, embed=embed)

        match = re.match("^SAN([0-9]+)$", message.content)
        if match:
            border = int(match.groups()[0])
            dice = randint(1, 100)
            if dice <= border:
                title = "成功"
                color = discord.Colour.green()
            else:
                title = f"失敗"
                color = discord.Colour.red()
            embed = discord.Embed(
                title=title,
                description=f"SAN値チェック（1d100）= **{dice}**",
                color=color
            )
            await message.channel.send(reference=message, mention_author=True, embed=embed)

        match = re.match("^ccb<=([0-9]+).*$", str(message.content).lower())
        if match:
            border = int(match.groups()[0])
            dice = randint(1, 100)
            if dice <= border:
                title = "成功"
                if dice <= 5:
                    title = "クリティカル"
                color = discord.Colour.green()
            else:
                title = f"失敗"
                if dice >= 96:
                    title = "ファンブル"
                color = discord.Colour.red()
            embed = discord.Embed(
                title=title,
                description=f"技能チェック（1d100）= **{dice}**",
                color=color
            )
            await message.channel.send(reference=message, mention_author=True, embed=embed)

    @slash_client.slash(
        name="secret",
        guild_ids=servers,
        description="D100でシークレットダイスを振ります"
    )
    async def _slash_secret(ctx: SlashContext):
        await ctx.send(content="結果：`{0}`".format(randint(1, 100)), hidden=True)

    @slash_client.slash(
        name="omikuji",
        guild_ids=servers,
        description="今年の運勢を占ってみましょう！"
    )
    async def _slash_omikuji(ctx: SlashContext):
        total = choice(omikuji)
        result = "{0}\n願望{1}　仕事{2}　恋愛{3}\n健康{4}　金運{5}　旅行{6}".format(
            total,
            choice(unsei), choice(unsei), choice(unsei),
            choice(unsei), choice(unsei), choice(unsei)
        )
        embed = discord.Embed(
            title="【おみくじ】",
            description=result,
            color=discord.Colour.green()
        )
        await ctx.send(embed=embed)

    @ slash_client.slash(
        name="coc",
        guild_ids=servers,
        description="CoCのキャラシを作成します"
    )
    async def _slash_coc(ctx: SlashContext):
        STR = randint(1, 6) + randint(1, 6) + randint(1, 6)
        CON = randint(1, 6) + randint(1, 6) + randint(1, 6)
        POW = randint(1, 6) + randint(1, 6) + randint(1, 6)
        DEX = randint(1, 6) + randint(1, 6) + randint(1, 6)
        APP = randint(1, 6) + randint(1, 6) + randint(1, 6)
        SIZ = randint(1, 6) + randint(1, 6) + 6
        INT = randint(1, 6) + randint(1, 6) + 6
        EDU = randint(1, 6) + randint(1, 6) + randint(1, 6) + 3
        result = CoC_CharacterSheet.format(
            STR, CON, POW, DEX, APP, SIZ, INT, EDU,
            POW*5, POW*5, INT*5, EDU*5, (CON+SIZ)//2,
            EDU*20, INT*10
        )
        embed = discord.Embed(
            title="CoCキャラシ生成結果",
            url=f"https://iachara.com/new/costom/webdice?var=6&STR={STR}&CON={CON}&POW={POW}&DEX={DEX}&APP={APP}&SIZ={SIZ}&INT={INT}&EDU={EDU}",
            description=result,
            color=discord.Colour.green()
        )
        embed.set_footer(
            text="最上部のリンクをクリックすると、このダイス結果で「いあきゃら」のキャラクターを作成します")
        await ctx.send(embed=embed)

    @slash_client.slash(
        name="tokucho",
        guild_ids=servers,
        description="特徴表からランダムに1つ表示します"
    )
    async def _slash_tokucho(ctx: SlashContext):
        roll = (0, randint(1, 6), randint(1, 10))
        result = tokucho[roll[1]][roll[2]]
        embed = discord.Embed(
            title=f"特徴表ロール結果：{roll[1]}-{roll[2]}『{result[0]}』",
            description=result[1],
            color=discord.Colour.blue()
        )
        await ctx.send(embed=embed)

    client.run(TOKEN)
