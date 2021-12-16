# Tardsquad Discord Bot
[![PyPI version](https://badge.fury.io/py/tardsquad-discord-bot.svg)](https://badge.fury.io/py/tardsquad-discord-bot)
[![Downloads](https://pepy.tech/badge/tardsquad-discord-bot)](https://pepy.tech/project/tardsquad-discord-bot)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/tardsquad-discord-bot)](#)
[![Travis Build Status](https://img.shields.io/travis/com/erikw/tardsquad-discord-bot/master?logo=travis)](https://app.travis-ci.com/github/erikw/tardsquad-discord-bot)
[![SLOC](https://img.shields.io/tokei/lines/github/erikw/tardsquad-discord-bot)](#)
[![License](https://img.shields.io/pypi/l/tardsquad-discord-bot)](https://github.com/erikw/tardsquad-discord-bot/blob/master/LICENSE)
[![OSS Lifecycle](https://img.shields.io/osslifecycle/erikw/tardsquad-discord-bot)](https://github.com/Netflix/osstracker)


# Resouces
* Discord [Developer Portal](https://discordapp.com/developers/applications)
* A general tutorial for a Discord bot can be found [here](https://realpython.com/how-to-make-a-discord-bot-python/)

# Setup
## Installation
Make sure to use a supported python version. See the key `python` in the section `tool.poetry.dependencies` at [pyproject.toml](https://github.com/erikw/tardsquad-discord-bot/blob/master/pyproject.toml).

```console
$ pip install tardsquad-discord-bot
$ tardsquad-discord-bot -h
```

If you use [pipx](https://pypi.org/project/pipx/) to install, you must specify a supported and locally available python version like:

```console
$ pipx install --python python3.9  tardsquad-discord-bot
```

To use this tool, you need to supply
* `--url` to your taiga server e.g. `https://api.taiga.io/`
* `--auth-token` that you need to obtain according to the [official instructions](https://docs.taiga.io/api.html#_authentication).

It's recommended to put these 2 values in the below described `tardsquad-discord-bot.conf` file for easier usage of this tool!


# Development
* Make sure to `$ poetry shell` before using tools like pyright LSP, so that it can find the installed dependency modules
* Reference for how to structure a python project: https://realpython.com/pypi-publish-python-package/

## Setup from Git
* Clone this git
```console
$ git clone https://github.com/erikw/tardsquad-discord-bot.git
$ cd tardsquad-discord-bot
```
* Install Poetry
* Numpy install issues as of 2021-10-31
* `$ poetry install` did not work with Numpy on macOS. Solution from https://github.com/python-poetry/poetry/issues/3196#issuecomment-769753478
```console
$ pyenv local 3.9.7
$ poetry env use 3.9.7
$ poetry config experimental.new-installer false
$ poetry install
```

* Install dependencies
```console
$ poetry install
```
* Now tardsquad-discord-bot should work!
```console
$ poetry run tardsquad-discord-bot -h
$ # or
$ bin/tardsquad-discord-bot.sh
```
* To install locally:
```console
$ poetry build
$ pip install dist/taiga_stats-*.whl
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

or

```console
$ vi -p pyproject.toml CHANGELOG.md  # Update version.
$ poetry publish --build
```
