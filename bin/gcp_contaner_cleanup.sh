#!/usr/bin/env bash
# Implementation of "retention policy" of built contaienrs at
# https://console.cloud.google.com/gcr/images/tardsquad-discord-bot/global/tardsquad-discord-bot?project=tardsquad-discord-bot
# Ref: https://serverfault.com/a/952644

IMAGE_NAME=gcr.io/tardsquad-discord-bot/tardsquad-discord-bot
RETENTION_IMAGES=5  # Keep X latest images.

digests=$(gcloud container images list-tags $IMAGE_NAME --format=json | awk '/digest/{ print $2 }' | sed -e 's/^"//' -e 's/.\{2\}$//' | tail -n +$((RETENTION_IMAGES+1)))
test -n "$digests" || exit 0

for digest in "$digests"; do
	gcloud container images -q delete $IMAGE_NAME@$digest
done
