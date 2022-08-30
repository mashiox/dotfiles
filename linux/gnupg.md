# GnuPG

## Getting Started

Invoke the wizard using the command:

```bash
$ gpg --full-generate-key
```

The user's email is typically assigned as the gpg id.
It will ask for a passphrase at the last step, please record it!

## Backing up secrets

```bash
chown -R $USER:$GROUP ~/.gnupg

# Export key by ID
gpg --export-secret-keys [key-id] >secret-keys.gpg

# Recover keys from old key location
gpg --homedir /path/to/backup/.gnupg --list-secret-keys

# list the secret keys
gpg --homedir /path/to/.gnupg --export-secret-keys [key-id] > secret-keys.gpg

# Import keys to new GnuPG keyring
gpg --homedir /path/to/.gnupg --export-secret-keys [key-id] | gpg --import
```

## Reference

- https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG_002dAGENT.html
- https://superuser.com/a/1009783
