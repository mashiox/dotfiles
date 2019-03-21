# Git Configuration files and notes

## My Tips and Tricks

Switching between branches with changes committed, with WIP work uncommitted
```bash
# Stash changes with some contexual identifier and a comment
$ git stash save "<WTQ-123 or branch name> Refactoring auth code"

$ git checkout different-branch

# Lists all stash saves, with the comment.
$ git stash list

# Apply the changes from relevant stash@{#}
$ git stash pop stash@{1}

```

Generating a patch file from git diffs, and applying that on a different system
```bash
# Get code diff reletave to our position in the code's filesystem
$ git diff

# Get the code diff, write the diff to our patch file
$ git diff > my_diff.patch

# Apply the patch to the code, from the same position in the file system
$ patch -p1 < ./my_diff.patch
```

## Basic Usage 

```bash
$ git config --global alias.co checkout
$ git config --global alias.br branch
$ git config --global alias.ci commit
$ git config --global alias.st status
```
