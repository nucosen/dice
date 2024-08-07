from setuptools import setup, find_packages

# NOTE : Version here
setup(
    name="dice",
    version="6.3.0",
    description="Discord dice bot",
    author="NUCOSen Management Committee",
    author_email="info@nucosen.live",
    url="https://github.com/nucosen/dice",
    packages=find_packages(),
    entry_points={"console_scripts": ["dice = dice.cli:execute"]},
    install_requires=open("requirements.txt", encoding="utf-16").read().splitlines(),
    license="MIT License",
)
