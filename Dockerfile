# Reference on Poetry in Docker: https://stackoverflow.com/a/54763270/265508

FROM python:3.10-slim
LABEL maintainer="erik.westrup@gmail.com"
LABEL vendor="tardsquad"

# Python
ENV \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONDONTWRITEBYTECODE=1
# pip
ENV \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100
# Poetry
ENV \
  POETRY_VERSION=1.1.11 \
  POETRY_NO_INTERACTION=1 \
  PATH="$PATH:/root/.local/bin"

# System dependencies
RUN apt-get update \
	&& apt-get upgrade -y \
	&& apt-get install --no-install-recommends -y \
		bash \
		build-essential \
		curl \
  # Installing `poetry` package manager:
  && pip install "poetry==$POETRY_VERSION" \
  # Official way is with curl, but it has cons as well..
  #&& curl -sSL 'https://install.python-poetry.org' | python - \
  && poetry --version \
  # Cleaning cache
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && apt-get clean -y && rm -rf /var/lib/apt/lists/*

WORKDIR /code

# Copy only requirements to cache them in docker layer
WORKDIR /code
COPY . /code/


# Project initialization:
RUN poetry install --no-dev --no-ansi

# We customize how our app is loaded with the custom entrypoint:
ENTRYPOINT ["poetry", "run", "tardsquad-discord-bot"]
