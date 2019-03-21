# Notes on configuring Visual Studio Code

## PHP Debugging

See the section in this repo on [XDebug](../xdebug)

## Rsync

[Sync-Rsync from @thisboyiscrazy](https://marketplace.visualstudio.com/items?itemName=vscode-ext.sync-rsync)

https://github.com/thisboyiscrazy/vscode-rsync

My guidelines for operational success using rsync in VSCode. 

* Use a `[project-name]/[domain]-rsync` naming convention
  * `mashio.net/devServer-rsync
* Favor syncing to local (down)
  * Create new directories on the server and sync down
  * Add new static files to project and sync them up.
* Disable sync on save and sync on file open on sensitive sites
* Excluse `.git/` and commit to doing git commits on the original source
