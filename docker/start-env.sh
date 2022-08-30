#!/usr/bin/env bash

# Debug output
set -x

# Options
SECRET_HOME="/mnt/secrets"
SECRET_NAME="www.env"

# RAM-only space
stat $SECRET_HOME
if [[ "0" != $? ]] then
	mount -t tmpfs -o size=500m tmpfs $SECRET_HOME
	chmod 0600 $SECRET_HOME
fi

# Recover secret
pass $SECRET_NAME > "$SECRET_HOME/$SECRET_NAME"

# Start docker environment
docker-compose up -d
