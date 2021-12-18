# Tardsquad Discord Bot
[![Push to GCR GitHub Action](https://github.com/Tardsquad/tardsquad-discord-bot/actions/workflows/push_to_gcr.yml/badge.svg)](https://github.com/Tardsquad/tardsquad-discord-bot/actions/workflows/push_to_gcr.yml)
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
* GCP
  * [Container Registry](https://console.cloud.google.com/gcr/images/tardsquad-discord-bot?project=tardsquad-discord-bot)
  * [Storage Bucket](https://console.cloud.google.com/storage/browser?project=tardsquad-discord-bot&prefix=) for the above containers
  * [Service Account](https://console.cloud.google.com/iam-admin/serviceaccounts/details/100468477191441270091?project=tardsquad-discord-bot&supportedpurview=project) used to publish Docker images to GCR.
  * [Cloud Run Service](https://console.cloud.google.com/run/detail/us-central1/tardsquad-discord-bot/metrics?project=tardsquad-discord-bot) that runs our container for image published to GCR.
  * [Secret Manager](https://console.cloud.google.com/security/secret-manager/secret/) is where `DISCORD_TOKEN` is stored, which is hooked up as envvar in the Cloud Run service.

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

## TL;DR the easy way
* Get the discord token by asking [@erikw](https://github.com/erikw) or from the bot tab in the [tardsquad-discord-bot](https://discord.com/developers/applications/921085762190057532/bot) application in the Discord developer portal
```console
$ git clone https://github.com/tardsquad/tardsquad-discord-bot.git && cd $(basename "$_" .git)
$ echo "DISCORD_TOKEN=the-token" > .env
$ docker-compose up
```

Continue reading for how to setup local development envionment, with our without Docker below:

## More elaborate
* Make sure to `$ poetry shell` before using tools like pyright LSP, so that it can find the installed dependency modules
* Reference for how to structure a python project: https://realpython.com/pypi-publish-python-package/

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

* Build and run Docker image using the local `.env` file with secrets:
```console
$ docker build -t tardsquad-discord-bot .
$ docker run --env-file=.env -t tardsquad-discord-bot
$ # or more simply
$ docker-compose up
```

* Drop in to a shell like
```console
$ docker run --env-file=.env --rm -it --entrypoint bash tardsquad-discord-bot
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
