# Docker Secrets

This document outlines a strategy to pass secrets to docker compose environments without exposing the secrets in plain text.

## Prerequisites

- [GnuPG](linux/gnupg.md)
- [Pass](linux/pass.md)

## Steps

Scenario: We want to load a docker environment file from RAM when the container environment starts.

Initialize RAM-only filesystem space

```bash
mount -t tmpfs -o size=500m tmpfs /mnt/secrets/
chmod 0600 /mnt/secrets
```

Load secrets into RAM

```bash
pass Test/docker-www.env > /mnt/secrets/www.env
```

Start docker services.

```yaml
version: "3"

services:
    client:
        image: nginx
        ports:
            - 8420:80
        env_file:
            - /mnt/secrets/www.env
```

```bash
$ docker-compose up -d
$ docker-compose exec client bash
> env
```
