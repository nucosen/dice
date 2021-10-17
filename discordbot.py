import discord
import re
from random import randint, choice
import os

import configparser
from logging import INFO, basicConfig, getLogger

from json import load

basicConfig(
    format='{asctime} [{levelname:.4}] {name}: {message}',
    style='{'
)
logger = getLogger(__name__)
logger.info("Start dice-KUN")

config = configparser.ConfigParser()
baseDirectory = os.getcwd() + f"{os.sep}config{os.sep}"
optionFilePath = baseDirectory + "options.ini"
logger.info("Config parser loaded")

client = discord.Client()
logger.info("Discord client loaded")

config.read([optionFilePath])
if not config.has_section("LICENSE"):
    config.add_section("LICENSE")
licenseConfig = config["LICENSE"]
logger.info("Main option file loaded")

agreement = licenseConfig.getboolean("Agreement")
if agreement is None or not agreement:
    logger.critical("License not agreed")
    print("最初にsetup.pyを実行してください。")
    print('Run setup.py first.')
    exit()
logger.info("License agreed")

TOKEN = config.get("Discord", "token")

CoC_CharacterSheet = """```\
STR（3d6）  ：{0}
CON（3d6）  ：{1}
POW（3d6）  ：{2}
DEX（3d6）  ：{3}
APP（3d6）  ：{4}
SIZ（2d6+6）：{5}
INT（2d6+6）：{6}
EDU（3d6+3）：{7}
--------------------
SAN（POWx5）    ：{8}
幸運（POWx5）   ：{9}
アイデア（INTx5）   ：{10}
知識（EDUx5）       ：{11}
耐久力（CON+SIZ /2）：{12}
--------------------
職業P（EDUx20） ：{13}
興味P（INTx10） ：{14}
```"""

Guide = """```\
（※ xx や yy は半角数値に置き換えてください）

文章中に「xxdyy!」　指定されたダイスに置き換えられます

「CoC」　CoCのキャラシ生成
        気に入ったキャラシは「いあきゃら」で保存できます

「SANxx」　SAN値xxでSAN値チェック。

「CCB<=xx」
「CCB<=xx【技能名】」
　　　技能値チェック。
　　　成功／失敗だけでなくクリティカル／ファンブルも出ます

「特徴表」
　　　特徴表に沿ってダイスロールを行います
　　　表番号と特徴名、効果を表示します

「@ダイス君」　このガイドを表示します\
```"""


@client.event
async def on_message(message):

    if isinstance(message, discord.Message):
        if message.author.bot:
            return

        if client.user in message.mentions:
            emoji_list = [
                "\N{GRINNING FACE}",
                "\N{GRINNING FACE WITH SMILING EYES}",
                "\N{SMILING FACE WITH OPEN MOUTH}",
                "\N{SMILING FACE WITH OPEN MOUTH AND SMILING EYES}",
                "\N{SMILING FACE WITH OPEN MOUTH AND TIGHTLY-CLOSED EYES}",
                "\N{WINKING FACE}",
                "\N{SMILING FACE WITH SMILING EYES}",
                "\N{FACE SAVOURING DELICIOUS FOOD}",
                "\N{SMILING FACE WITH SUNGLASSES}",
                "\N{SMIRKING FACE}"
            ]
            await message.add_reaction(choice(emoji_list))
            embed = discord.Embed(
                title="「ダイス君」で出来ること",
                description=Guide,
                color=discord.Colour.blue()
            )
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
            DICE_ROLLED = True
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

        match = re.match("^CCB<=([0-9]+).*$", message.content)
        if match:
            DICE_ROLLED = True
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

        if message.content == "特徴表":
            DICE_ROLLED = True
            roll = (0, randint(1, 6), randint(1, 10))
            with open(os.getcwd() + f"{os.sep}db{os.sep}tokucho.json", "r", encoding="utf-8") as fp:
                result = load(fp)[roll[1]][roll[2]]
            embed = discord.Embed(
                title=f"特徴表ロール結果：{roll[1]}-{roll[2]}『{result[0]}』",
                description=result[1],
                color=discord.Colour.blue()
            )
            await message.channel.send(reference=message, mention_author=True, embed=embed)

        if message.content == "CoC":
            DICE_ROLLED = True
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
            await message.channel.send(reference=message, mention_author=True, embed=embed)

        if message.content == "TESTING DICE-KUN":
            embed = discord.Embed(
                title="ダイス君は正常に動作しています",
                description=f"デバッグの際はロギングレベルをINFOに下げてください",
                color=discord.Colour.green()
            )
            logger.info("=== Received the testing message ===")
            await message.channel.send(reference=message, mention_author=True, embed=embed)


client.run(TOKEN)
