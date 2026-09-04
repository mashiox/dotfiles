# Docker Secrets

This document outlines a strategy to pass secrets to docker compose environments without exposing the secrets in plain text.

## Prerequisites

- [GnuPG](/linux/gnupg.md)
- [Pass](/linux/pass.md)

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

Command Line
```bash
docker run -d \
  --name client \
  -p 8420:80 \
  --env-file /mnt/secrets/www.env \
  nginx

docker exec -it client env

docker exec client printenv your_secret_key
```

Compose definition:
```yaml
services:
    client:
        image: nginx
        ports:
            - 8420:80
        env_file:
            - /mnt/secrets/www.env
```

```bash
$ docker compose up -d
$ docker compose exec client bash
> env
```
