from json import loads
from requests import get, post
try:
    from dice.text import *
    from dice.discord_slash import SlashCommand, SlashContext
    from dice.discord_slash.utils.manage_commands import create_option
except ModuleNotFoundError:
    from text import *
    from discord_slash import SlashCommand, SlashContext
    from discord_slash.utils.manage_commands import create_option
from typing import List
import discord
import re
from random import randint, choice
import os
from logging import basicConfig, getLogger, INFO
from decouple import UndefinedValueError, AutoConfig
from discord.ext import commands
from time import sleep
import pyotp
import base64

basicConfig(
    format='{asctime} [{levelname:4}] {message}',
    style='{',
    level=INFO
)


def run():
    logger = getLogger(__name__)

    client = commands.Bot(command_prefix='@', intents=discord.Intents.all())
    slash_client = SlashCommand(client, sync_commands=True)

    # NOTE : Version here
    logger.info(dicelogo)
    logger.info("Starting : Dice-kun v6.2.1")
    for count in range(5, 0, -1):
        logger.info(str(count) + "...")
        sleep(1)

    try:
        config = AutoConfig(search_path=os.getcwd())
        TOKEN = config("DISCORD_DICE_TOKEN")
    except UndefinedValueError:
        logger.critical("Discord token is NOT FOUND.")
        exit()

    try:
        totp = pyotp.TOTP(str(config("TOTP")))
    except UndefinedValueError:
        totp = pyotp.TOTP("SAMPLEsample")

    try:
        servers: List = str(config("DISCORD_DICE_SERVERS")).split(",")
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

        if client.user in message.mentions:
            await message.add_reaction(choice(emoji_list))
            # NOTE : Version here
            embed = discord.Embed(
                title="??????????????? v6.2.1?????????????????????",
                description=Guide,
                color=discord.Colour.blue()
            )
            logger.info("Dice-kun is active !")
            await message.channel.send(embed=embed)
            return

        if match := re.search("^!(.+)", message.content):
            box = match.groups()[0].replace("???", " ").strip().split(" ")
            embed = discord.Embed(
                title="????????????",
                description=choice(box),
                color=discord.Color.green()
            )
            await message.channel.send(reference=message, mention_author=True, embed=embed)

        if match := re.search("([0-9]{1,4})d([0-9]{1,4})!", message.content):
            await message.add_reaction("\N{GAME DIE}")
            resultMessage = message.content
            additionalMessage = ""
            rolledDiceList = []
            while True:
                count = int(match.groups()[0])
                randmax = int(match.groups()[1])
                if count == 0 and randmax == 0:
                    additionalMessage = "\n\n???ID???`{0}`\n\n???????????????`{1}`".format(
                        message.guild.id if message.guild is not None else "????????????",
                        totp.now()
                    )
                else:
                    additionalMessage = ""
                result = 0
                if count != 0 and randmax != 0:
                    for _ in range(count):
                        result += randint(1, randmax)
                resultMessage = resultMessage.replace(
                    match.group(), f" `{result}` ", 1
                )
                rolledDiceList.append(match.group()[:-1] + f"???**{result}**")
                if not (match := re.search("([0-9]{1,4})d([0-9]{1,4})!", resultMessage)):
                    break
            embed = discord.Embed(
                title="Dice Roll",
                description=resultMessage + "\n" +
                "\n".join(rolledDiceList) + additionalMessage,
                color=discord.Color.green()
            )
            await message.channel.send(reference=message, mention_author=True, embed=embed)

        match = re.match("^san([0-9]+)$", str(message.content).lower())
        if match:
            border = int(match.groups()[0])
            dice = randint(1, 100)
            if dice <= border:
                title = "??????"
                color = discord.Colour.green()
            else:
                title = f"??????"
                color = discord.Colour.red()
            embed = discord.Embed(
                title=title,
                description=f"SAN??????????????????1d100???= **{dice}**",
                color=color
            )
            await message.channel.send(reference=message, mention_author=True, embed=embed)

        match = re.match("^ccb([0-9]+).*$", str(message.content).lower())
        if match:
            border = int(match.groups()[0])
            dice = randint(1, 100)
            if dice <= border:
                title = "??????"
                if dice <= 5:
                    title = "??????????????????"
                color = discord.Colour.green()
            else:
                title = "??????"
                if dice >= 96:
                    title = "???????????????"
                color = discord.Colour.red()
            embed = discord.Embed(
                title=title,
                description=f"?????????????????????1d100???= **{dice}**",
                color=color
            )
            await message.channel.send(reference=message, mention_author=True, embed=embed)

    shindan_option = create_option(
        name="name",
        description="????????????????????????????????????????????????",
        option_type=str,
        required=True
    )

    @slash_client.slash(
        name="shindan",
        guild_ids=servers,
        description="?????????????????????????????????",
        options=[shindan_option]
    )
    async def _slash_shindan(ctx: SlashContext, name: str):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0"
        }
        search = get(
            "https://shindanmaker.com/list/search?q={0}".format(name),
            headers=headers
        )
        search.raise_for_status()
        match = re.search(
            "https?://shindanmaker.com/([0-9]+)", str(search.text))
        if "????????????????????????????????????????????????" in search.text or match is None:
            await ctx.send(content="????????????????????????????????????????????????", hidden=True)
            return
        url = str(match.group())
        shindan = get(
            url,
            headers=headers
        )
        shindan.raise_for_status()
        match = re.search(
            '<input type="hidden" name="_token" value="([^"]+)">',
            str(shindan.text)
        )
        if match is None:
            raise Exception("????????????????????????")
        name = str(ctx.author)[:-5]
        token = match.groups()[0]
        result = post(
            url,
            params={
                "_token": token,
                "shindanName": name,
            },
            headers=headers,
            cookies=shindan.cookies
        )
        shindan_result = re.search(
            '<textarea id="share-copytext-shindanresult-textarea" style="display: none;">([^<]+)</textarea>',
            result.text
        )
        title = re.search(
            '<title>([^<]+)</title>',
            result.text
        )
        if shindan_result is None or title is None:
            raise Exception("??????????????????????????????????????????")
        embed = discord.Embed(
            title=title.groups()[0],
            description=re.sub(
                "&(?:[^;]+);", "", shindan_result.groups()[0].replace("&#10;", "\n")),
            color=discord.Colour.blue()
        )
        await ctx.send(embed=embed)

    @slash_client.slash(
        name="secret",
        guild_ids=servers,
        description="D100?????????????????????????????????????????????"
    )
    async def _slash_secret(ctx: SlashContext):
        await ctx.send(content="?????????`{0}`".format(randint(1, 100)), hidden=True)

    yesno_option = create_option(
        name="small",
        description="True????????????????????????????????????",
        option_type=bool,
        required=False
    )

    @slash_client.slash(
        name="yesno",
        guild_ids=servers,
        description="???????????????Yes???No???????????????????????????",
        options=[yesno_option]
    )
    async def _slash_yesno(ctx: SlashContext, small: bool = False):
        result = loads(get("https://yesno.wtf/api").text)
        if small:
            result_text: str = result["answer"]
            await ctx.send(content=result_text.capitalize()+"!")
        else:
            await ctx.send(content=result["image"])

    touhou_option = create_option(
        name="repeats",
        description="???????????????????????????????????????????????????",
        option_type=int,
        required=False
    )

    @slash_client.slash(
        name="touhou",
        guild_ids=servers,
        description="??????Project??????????????????????????????????????????",
        options=[touhou_option]
    )
    async def _slash_touhou(ctx: SlashContext, repeats: int = 1):
        results: List[str] = []
        if repeats < 1 or repeats >= 100:
            repeats = 1
            results.append("`???????????????????????????????????????1??????100??????????????????????????????????????????`")
        for _ in range(repeats):
            results.append(choice(touhou_character))
        result = "\n".join(results)
        embed = discord.Embed(
            title="????????????????????????",
            description=result,
            color=discord.Colour.blue()
        )
        await ctx.send(embed=embed)

    @slash_client.slash(
        name="omikuji",
        guild_ids=servers,
        description="?????????????????????????????????????????????"
    )
    async def _slash_omikuji(ctx: SlashContext):
        total = choice(omikuji)
        result = "{0}\n??????{1}?????????{2}?????????{3}\n??????{4}?????????{5}?????????{6}".format(
            total,
            choice(unsei), choice(unsei), choice(unsei),
            choice(unsei), choice(unsei), choice(unsei)
        )
        embed = discord.Embed(
            title="?????????????????????",
            description=result,
            color=discord.Colour.green()
        )
        await ctx.send(embed=embed)

    @ slash_client.slash(
        name="coc",
        guild_ids=servers,
        description="CoC?????????????????????????????????"
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
            title="CoC????????????????????????",
            url=f"https://iachara.com/new/costom/webdice?var=6&STR={STR}&CON={CON}&POW={POW}&DEX={DEX}&APP={APP}&SIZ={SIZ}&INT={INT}&EDU={EDU}",
            description=result,
            color=discord.Colour.green()
        )
        embed.set_footer(
            text="????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????"  # type: ignore
        )
        await ctx.send(embed=embed)

    @slash_client.slash(
        name="tokucho",
        guild_ids=servers,
        description="??????????????????????????????1??????????????????"
    )
    async def _slash_tokucho(ctx: SlashContext):
        roll = (0, randint(1, 6), randint(1, 10))
        result = tokucho[roll[1]][roll[2]]
        embed = discord.Embed(
            title=f"???????????????????????????{roll[1]}-{roll[2]}???{result[0]}???",
            description=result[1],
            color=discord.Colour.blue()
        )
        await ctx.send(embed=embed)

    client.run(TOKEN)


if __name__ == "__main__":
    run()
