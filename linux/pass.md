# Pass

Unix Password manager https://www.passwordstore.org/

## Getting Started

Init password repository in `~/.password-store`

Requires [GnuPG ID](./gnupg.md)

```bash
pass init [gnupg-key-id]

# Add git repository
pass git init

pass git remote add origin git@example.com:git/git.git

# Generate 10-symbol password
pass generate 2022-241-test 10

# Generate 10-symbol alpha password
pass generate -n 2022-241-test 10

# Insert new secret phrase
pass insert Test/secret

# Insert new secret document
pass insert -m Test/secret.cfg

# Print secret
pass Test/secret

# Print secret document to RAM
mount -t tmpfs -o size=500m tmpfs /mnt/pass/
pass Test/secret.cfg > /mnt/pass/secret.cfg
```

## References

- https://git.zx2c4.com/password-store/about/#EXTENDED%20GIT%20EXAMPLE
- https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG_002dAGENT.html
