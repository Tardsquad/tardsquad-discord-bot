# Reference: https://stackoverflow.com/a/54763270/265508
FROM python:3.10-slim
LABEL maintainer="eri.westrup@gmail.com"
LABEL vendor="tardsquad"

#ARG MY_ENV

ENV \
  # python:
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  # pip:
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # dockerize:
  DOCKERIZE_VERSION=v0.6.1 \
  # poetry:
  POETRY_VERSION=1.1.11 \
  POETRY_NO_INTERACTION=1 \
  # TODO venvs are good after all in docker? https://github.com/python-poetry/poetry/issues/4493
  #POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  PATH="$PATH:/root/.local/bin"


# System deps:
RUN apt-get update && apt-get upgrade -y \
  && apt-get install --no-install-recommends -y \
    bash \
    build-essential \
    curl \
  # Installing `poetry` package manager:
  && pip install "poetry==$POETRY_VERSION" \
  #&& curl -sSL 'https://install.python-poetry.org' | python - \
  && poetry --version \
  # Cleaning cache:
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && apt-get clean -y && rm -rf /var/lib/apt/lists/*

WORKDIR /code

# Copy only requirements to cache them in docker layer
WORKDIR /code
COPY poetry.lock pyproject.toml /code/


# Project initialization:
RUN poetry install --no-dev --no-ansi
  # Cleaning poetry installation's cache
  #&& rm -rf "$POETRY_CACHE_DIR"

# Creating folders, and files for a project:
COPY tardsquad_discord_bot/ /code/tardsquad_discord_bot
COPY CHANGELOG.md LICENSE README.md /code

# We customize how our app is loaded with the custom entrypoint:
ENTRYPOINT ["poetry", "run", "tardsquad-bot"]