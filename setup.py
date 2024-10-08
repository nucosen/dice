from setuptools import setup, find_packages

setup(
    name="dice",
    version=open("dice/text.py", encoding="utf-8").read().splitlines()[0].split('"')[1],
    description="Discord dice bot",
    author="NUCOSen Management Committee",
    author_email="info@nucosen.live",
    url="https://github.com/nucosen/dice",
    packages=find_packages(),
    entry_points={"console_scripts": ["dice = dice.cli:execute"]},
    install_requires=open("requirements.txt", encoding="utf-16").read().splitlines(),
    license="MIT License",
)
