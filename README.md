# Tardsquad Discord Bot
[![PyPI version](https://badge.fury.io/py/tardsquad-discord-bot.svg)](https://badge.fury.io/py/tardsquad-discord-bot)
[![Downloads](https://pepy.tech/badge/tardsquad-discord-bot)](https://pepy.tech/project/tardsquad-discord-bot)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/tardsquad-discord-bot)](#)
[![Travis Build Status](https://img.shields.io/travis/com/tardsquad/tardsquad-discord-bot/master?logo=travis)](https://app.travis-ci.com/github/tardsquad/tardsquad-discord-bot)
[![SLOC](https://img.shields.io/tokei/lines/github/tardsquad/tardsquad-discord-bot)](#)
[![License](https://img.shields.io/pypi/l/tardsquad-discord-bot)](https://github.com/tardsquad/tardsquad-discord-bot/blob/master/LICENSE)
[![OSS Lifecycle](https://img.shields.io/osslifecycle/tardsquad/tardsquad-discord-bot)](https://github.com/Netflix/osstracker)

A Discord chat bot for the Tardsquad guild (Discord name for server).

# Resouces
* Discord [Developer Portal](https://discordapp.com/developers/applications)
* A general tutorial for a Discord bot can be found [here](https://realpython.com/how-to-make-a-discord-bot-python/)

# Installation
Make sure to use a supported python version. See the key `python` in the section `tool.poetry.dependencies` at [pyproject.toml](https://github.com/tardsquad/tardsquad-discord-bot/blob/master/pyproject.toml).

```console
$ pip install tardsquad-discord-bot
$ tardsquad-bot
```

If you use [pipx](https://pypi.org/project/pipx/) to install, you must specify a supported and locally available python version like:

```console
$ pipx install --python python3.9 tardsquad-discord-bot
```

# Development
* Make sure to `$ poetry shell` before using tools like pyright LSP, so that it can find the installed dependency modules
* Reference for how to structure a python project: https://realpython.com/pypi-publish-python-package/

## Setup from Git
* Clone this git
```console
$ git clone https://github.com/tardsquad/tardsquad-discord-bot.git
$ cd tardsquad-discord-bot
```
* Install Poetry
```console
$ pip install poetry
```
* Install project dependencies
```console
$ poetry install
```

* Set up envionment. Fetch the bot token from the bot tab in the [tardsquad-discord-bot](https://discord.com/developers/applications/921085762190057532/bot) application in the Discord developer portal. Either set this as as an envionmental variable together with the guild (server name), or more preffered in the git-ignored `.env` file in the project directory:
```console
$ echo "DISCORD_TOKEN=the-token" > .env
$ echo "GUILD=tardsquad" >> .env
```

* Now tardsquad-discord-bot should work!
```console
$ poetry run tardsquad-discord-bot
```

* To install locally:
```console
$ poetry build
$ pip install dist/tardsquad_discord_bot-*.whl
```

* Build and run Docker image:
```console
$ docker build -t tardsquad-discord-bot .
$ docker run -t tardsquad-discord-bot
```

* Drop in to a shell like
```console
$ docker run --rm -it --entrypoint bash tardsquad-discord-bot
```


## Releasing
```console
$ vi -p pyproject.toml CHANGELOG.md  # Update version.
$ poetry build
$ ls -l dist/
$ git commit -m "Prepare vX.Y.Z"
$ git tag V.X.Y.Z
$ git push --all && git push --tags
$ poetry publish
```
