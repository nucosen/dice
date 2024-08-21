from json import loads
from requests import get, post

try:
    import dice.text as text
except ModuleNotFoundError:
    import text
from typing import List
import discord
from discord import app_commands as appcmd
import re
from random import randint, choice
import os
from logging import basicConfig, getLogger, INFO
from decouple import UndefinedValueError, AutoConfig
from time import sleep

basicConfig(format="{asctime} [{levelname:4}] {message}", style="{", level=INFO)


def run():
    logger = getLogger(__name__)

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(
        intents=intents,
    )

    logger.info(text.diceLogo)
    logger.info("Starting : Dice-kun " + text.version)
    # for count in range(5, 0, -1):
    #     logger.info(str(count) + "...")
    #     sleep(1)

    try:
        config = AutoConfig(search_path=os.getcwd())
        TOKEN = config("DISCORD_DICE_TOKEN")
    except UndefinedValueError:
        logger.critical("Discord token is NOT FOUND.")
        exit()

    tree = appcmd.CommandTree(client)

    async def setNewActivity(withMessage: bool = False):
        if(withMessage):
            await client.change_presence(
                activity=discord.CustomActivity(
                    choice(text.activities),
                    emoji=discord.PartialEmoji(name="\N{GAME DIE}"),
                )
            )
        else:
            await client.change_presence(activity=discord.CustomActivity(None))

    @client.event
    async def on_message(message):
        if client.user in message.mentions:
            await setNewActivity()
            await message.add_reaction(choice(text.emoji_list))
            embed = discord.Embed(
                title="「ダイス君 " + text.version + "」で出来ること",
                description=text.Guide,
                color=discord.Colour.blue(),
            )
            logger.info("Dice-kun is active !")
            await message.channel.send(embed=embed)
            return

        if match := re.search("^!(.+)", message.content):
            await setNewActivity()
            box = match.groups()[0].replace("　", " ").strip().split(" ")
            embed = discord.Embed(
                title="抽選結果", description=choice(box), color=discord.Color.green()
            )
            await message.channel.send(
                reference=message, mention_author=True, embed=embed
            )

        if match := re.search("([0-9]{1,4})d([0-9]{1,4})!", message.content):
            hasD100 = False
            await message.add_reaction("\N{GAME DIE}")
            resultMessage = message.content
            rolledDiceList = []
            while True:
                count = int(match.groups()[0])
                randMax = int(match.groups()[1])
                result = 0
                if count == 1 and randMax == 100:
                    hasD100 = True
                if count != 0 and randMax != 0:
                    for _ in range(count):
                        result += randint(1, randMax)
                resultMessage = resultMessage.replace(match.group(), f" `{result}` ", 1)
                rolledDiceList.append(match.group()[:-1] + f"：**{result}**")
                if not (
                    match := re.search("([0-9]{1,4})d([0-9]{1,4})!", resultMessage)
                ):
                    break
            embed = discord.Embed(
                title="Dice Roll",
                description=resultMessage + "\n" + "\n".join(rolledDiceList),
                color=discord.Color.green(),
            )
            await setNewActivity(hasD100)
            await message.channel.send(
                reference=message, mention_author=True, embed=embed
            )

        match = re.match("^san([0-9]+)$", str(message.content).lower())
        if match:
            await setNewActivity()
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
                color=color,
            )
            await message.channel.send(
                reference=message, mention_author=True, embed=embed
            )

        match = re.match("^ccb([0-9]+).*$", str(message.content).lower())
        if match:
            await setNewActivity()
            border = int(match.groups()[0])
            dice = randint(1, 100)
            if dice <= border:
                title = "成功"
                if dice <= 5:
                    title = "クリティカル"
                color = discord.Colour.green()
            else:
                title = "失敗"
                if dice >= 96:
                    title = "ファンブル"
                color = discord.Colour.red()
            embed = discord.Embed(
                title=title,
                description=f"技能チェック（1d100）= **{dice}**",
                color=color,
            )
            await message.channel.send(
                reference=message, mention_author=True, embed=embed
            )

    @tree.command(description="D100でシークレットダイスを振ります")
    async def secret(ctx: discord.Integration):
        await ctx.response.send_message(
            content="結果：`{0}`".format(randint(1, 100)), ephemeral=True
        )

    @tree.command(description="ダイス君がYesかNoで決断してくれます")
    @appcmd.describe(small="Trueにすると文字で返答します")
    async def yesno(ctx: discord.Integration, small: bool = False):
        result = loads(get("https://yesno.wtf/api").text)
        if small:
            result_text: str = result["answer"]
            await ctx.response.send_message(content=result_text.capitalize() + "!")
        else:
            await ctx.response.send_message(content=result["image"])

    # @tree.command(description="東方Projectからキャラクターを表示します")
    @appcmd.describe(repeats="表示するキャラクター数を指定します")
    async def touhou(ctx: discord.Integration, repeats: int = 1):
        results: List[str] = []
        if repeats < 1 or repeats >= 100:
            repeats = 1
            results.append(
                "`回数指定は無視されました。1以上100未満の値を指定してください。`"
            )
        for _ in range(repeats):
            results.append(choice(text.touhou_character))
        result = "\n".join(results)
        embed = discord.Embed(
            title="東方キャラダイス", description=result, color=discord.Colour.blue()
        )
        await ctx.response.send_message(embed=embed)

    @tree.command(description="今日の運勢を占ってみましょう！")
    async def omikuji(ctx: discord.Integration):
        total = choice(text.omikuji)
        result = "{0}\n願望{1}　仕事{2}　恋愛{3}\n健康{4}　金運{5}　旅行{6}".format(
            total,
            choice(text.unsei),
            choice(text.unsei),
            choice(text.unsei),
            choice(text.unsei),
            choice(text.unsei),
            choice(text.unsei),
        )
        embed = discord.Embed(
            title="【今日の運勢】", description=result, color=discord.Colour.green()
        )
        await ctx.response.send_message(embed=embed)

    @tree.command(description="CoCのキャラシを作成します")
    async def coc(ctx: discord.Integration):
        STR = randint(1, 6) + randint(1, 6) + randint(1, 6)
        CON = randint(1, 6) + randint(1, 6) + randint(1, 6)
        POW = randint(1, 6) + randint(1, 6) + randint(1, 6)
        DEX = randint(1, 6) + randint(1, 6) + randint(1, 6)
        APP = randint(1, 6) + randint(1, 6) + randint(1, 6)
        SIZ = randint(1, 6) + randint(1, 6) + 6
        INT = randint(1, 6) + randint(1, 6) + 6
        EDU = randint(1, 6) + randint(1, 6) + randint(1, 6) + 3
        result = text.CoC_CharacterSheet.format(
            STR,
            CON,
            POW,
            DEX,
            APP,
            SIZ,
            INT,
            EDU,
            POW * 5,
            POW * 5,
            INT * 5,
            EDU * 5,
            (CON + SIZ) // 2,
            EDU * 20,
            INT * 10,
        )
        embed = discord.Embed(
            title="CoCキャラシ生成結果",
            url=f"https://iachara.com/new/costom/webdice?var=6&STR={STR}&CON={CON}&POW={POW}&DEX={DEX}&APP={APP}&SIZ={SIZ}&INT={INT}&EDU={EDU}",
            description=result,
            color=discord.Colour.green(),
        )
        embed.set_footer(
            text="最上部のリンクをクリックすると、このダイス結果で「いあきゃら」のキャラクターを作成します"  # type: ignore
        )
        await ctx.response.send_message(embed=embed)

    @tree.command(description="特徴表からランダムに1つ表示します")
    async def tokucho(ctx: discord.Integration):
        roll = (0, randint(1, 6), randint(1, 10))
        result = text.tokucho[roll[1]][roll[2]]
        embed = discord.Embed(
            title=f"特徴表ロール結果：{roll[1]}-{roll[2]}『{result[0]}』",
            description=result[1],
            color=discord.Colour.blue(),
        )
        await ctx.response.send_message(embed=embed)

    @client.event
    async def on_ready():
        cmdList = await tree.sync()
        for cmd in cmdList:
            logger.info(cmd.name + " is synced !")
        logger.info("Dice-kun is ready !")

    client.run(TOKEN)


if __name__ == "__main__":
    run()
