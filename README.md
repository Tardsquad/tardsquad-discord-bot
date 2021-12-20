# Tardsquad Discord Bot
[![Discord Production](https://img.shields.io/discord/296746259358679040?color=success&label=production&logo=discord)](https://discord.gg/WHg5X5CvfV)
[![Discord Staging](https://img.shields.io/discord/921089193466277918?color=success&label=staging&logo=discord)](https://discord.gg/UkXYGmVEJp)
<br>
[![Latest SemVer Tag](https://img.shields.io/github/v/tag/tardsquad/tardsquad-discord-bot?sort=semver&label=Latest%20Release&logo=linuxcontainers)](https://github.com/Tardsquad/tardsquad-discord-bot/tags)
[![OSS Lifecycle](https://img.shields.io/osslifecycle/tardsquad/tardsquad-discord-bot)](https://github.com/Netflix/osstracker)
[![SLOC](https://img.shields.io/tokei/lines/github/tardsquad/tardsquad-discord-bot)](#)
[![License](https://img.shields.io/github/license/tardsquad/tardsquad-discord-bot)](https://github.com/tardsquad/tardsquad-discord-bot/blob/master/LICENSE)


A Discord chat bot for the Tardsquad guild (Discord name for server).

# Resouces
* A general tutorial for a Discord bot can be found [here](https://realpython.com/how-to-make-a-discord-bot-python/)
* [discord.py](https://github.com/Rapptz/discord.py) Python library to work with Discord
  * [API Reference](https://discordpy.readthedocs.io/en/latest/api.html#discord.Intents)
  * [Commands Refernce](https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html) from the extension module.
* Discord servers:
  * [Production](https://discord.gg/WHg5X5CvfV)
  * [Staging](https://discord.gg/UkXYGmVEJp)
* Discord [Developer Portal](https://discordapp.com/developers/applications)
  * [Application tardsquad-discord-bot-staging](https://discord.com/developers/applications/921085762190057532/information)
  * [Application tardsquad-discord-bot-production](https://discord.com/developers/applications/922195559618592799/information)
* GCP
  * [Cloud Run Service](https://console.cloud.google.com/run/detail/us-central1/tardsquad-discord-bot/metrics?project=tardsquad-discord-bot) that runs our container for image published to GCR.
  * [Cloud Build Triggers](https://console.cloud.google.com/cloud-build/triggers?referrer=search&project=tardsquad-discord-bot) Sets up build/push/deploy on git version tag push by pointing to [.google-cloud/cloudbuild.yaml](.google-cloud/cloudbuild.yaml).
  * [Container Registry](https://console.cloud.google.com/gcr/images/tardsquad-discord-bot?project=tardsquad-discord-bot)
    * [Storage Bucket](https://console.cloud.google.com/storage/browser?project=tardsquad-discord-bot&prefix=) for the above containers
  * [Service Account](https://console.cloud.google.com/iam-admin/serviceaccounts/details/100468477191441270091?project=tardsquad-discord-bot&supportedpurview=project) used to publish Docker images to GCR.
  * [Secret Manager](https://console.cloud.google.com/security/secret-manager/secret/) is where `DISCORD_TOKEN` is stored, which is hooked up as envvar in the Cloud Run service.



# Development
Make sure to use a supported python version. See the key `python` in the section `tool.poetry.dependencies` at [pyproject.toml](https://github.com/tardsquad/tardsquad-discord-bot/blob/master/pyproject.toml). It's recommended to install e.g. `pyenv` to manage python versions.

## TL;DR The Easy Way
* Get the discord token by asking [@erikw](https://github.com/erikw) or from the bot tab in the [tardsquad-discord-bot](https://discord.com/developers/applications/921085762190057532/bot) application in the Discord developer portal
```console
$ git clone https://github.com/tardsquad/tardsquad-discord-bot.git && cd $(basename "$_" .git)
$ echo "DISCORD_TOKEN=the-token" > .env
$ docker-compose up
```

Continue reading for how to setup local development envionment, with our without Docker below:

## More Elaborate
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

* Set up envionment. We must make sure to only use the staging envionment so that our local runs don't endup in production the server. Fetch the bot token from the bot tab in the [tardsquad-discord-bot-staging](https://discord.com/developers/applications/921085762190057532/bot) application in the Discord developer portal. Either set this as as an envionmental variable together with the guild (server name), or more preffered in the git-ignored `.env` file in the project directory:
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

* To pull a Docker image stored in Google Cloud Registry:
```console
$ brew install google-cloud-sdk
$ gcloud auth login
$ docker pull gcr.io/tardsquad-discord-bot/tardsquad-discord-bot:latest
```


# Release & Deploy
* First verify that the bot works
  ```console
  $ poetry run tardsquad-discord-bot
  $ docker-compose up
  ```
* Now update version and create corresponding git tag
  ```console
  $ vi -p pyproject.toml CHANGELOG.md  # Update version.
  $ git commit -m "Prepare vX.Y.Z"
  $ git tag V.X.Y.Z
  $ git push --all && git push --tags
  ```
* A newly pushed tag with the pattern `v.*` will trigger a [Cloud Build Triggers](https://console.cloud.google.com/cloud-build/triggers?referrer=search&project=tardsquad-discord-bot). This build trigger will execute [.google-cloud/cloudbuild.yaml](.google-cloud/cloudbuild.yaml). The last step will spin up a container for the new image at for the [Cloud Run Service](https://console.cloud.google.com/run/detail/us-central1/tardsquad-discord-bot/metrics?project=tardsquad-discord-bot) that runs our container for image published to GCR.
* Head over to the production discord and try a command like `!version` and it should work!

# Known Issues
* Even though the Cloud Run revision is configured to only have one container active at once, on a new deploymet the old one will live on for a while. This means that for some moment of time, multiple instances of the bot-client will be conntected and thus one will multiple replies on commands. Cloud Run is designed for web services, not chat bots :).
