import configparser
from logging import INFO, basicConfig, getLogger
import os
from getpass import getpass
import re

basicConfig(
    format='{asctime} [{levelname:.4}] {name}: {message}',
    style='{'
)
logger = getLogger(__name__)
logger.info("Start setup")

config = configparser.ConfigParser()
baseDirectory = os.getcwd() + f"{os.sep}config{os.sep}"
optionFilePath = baseDirectory + "options.ini"
logger.info("Config parser loaded")

config.read([optionFilePath])
if not config.has_section("LICENSE"):
    config.add_section("LICENSE")
licenseConfig = config["LICENSE"]
logger.info("Main option file loaded")

agreement = licenseConfig.getboolean("Agreement")
if agreement is None or not agreement:
    logger.warning("License not agreed")
    print("ライセンス文書に同意する場合、configフォルダ内のoptions.iniファイルを開いて「LICENSE」セクションの「Agreement」をyesに変更してください。")
    print('If you agree to the license document, open the options.ini file in the config folder and change the "Agreement" in the LICENSE section to yes.')
    licenseConfig["Agreement"] = "no"

else:
    logger.info("License agreed")
    if not config.has_section("Discord"):
        config.add_section("Discord")
    discordConfig = config["Discord"]
    if discordConfig.get("token", None) is None \
            or input("Would you change Discord access token ? (y/N): ") == "y":
        while True:
            accessToken = getpass("Enter Discord access token :")
            if re.match("^[0-9a-zA-Z._-]+$",accessToken):
                break
            print("Bad access token. You can use 0-9, a-z, A-z, and some symbols.")
        discordConfig["token"]
    pass

with open(optionFilePath, "w") as optionFilePoint:
    config.write(optionFilePoint)
logger.info("Main option file written")

logger.info("Setup is done")
print("Setup is done.")
