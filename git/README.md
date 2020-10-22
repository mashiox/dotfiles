# Git Configuration files and notes

## My Tips and Tricks

Switching between branches with changes committed, with WIP work uncommitted
```bash
# Stash changes with some contexual identifier and a comment
git stash save "<WTQ-123 or branch name> Refactoring auth code"

git checkout different-branch

# Lists all stash saves, with the comment.
git stash list

# Apply the changes from relevant stash@{#}
git stash pop stash@{1}

```

Generating a patch file from git diffs, and applying that on a different system
```bash
# Get code diff reletave to our position in the code's filesystem
git diff

# Get the code diff, write the diff to our patch file
git diff > my_diff.patch

# Apply the patch to the code, from the same position in the file system
patch -p1 < ./my_diff.patch
```

## Basic Usage 

```bash
git config --global alias.co checkout
git config --global alias.s status
git config --global aias.df diff
```

## Rebase

Rebasing is another way that a developer can keep a feature branch up-to-date with a parent branch. The way rebase does this is by re-writing all the unique commits on the feature branch, after removing them and writing all of the missing commits from the parent branch back onto the feature branch. This means all of your feature branch's commits will have new commit hashes. On successful rebase, the feature branch will appear to have a cleaner commit history, because the feature branch had been updated in such a way that it could have been created from the parent branch's `HEAD`.

### Recommended Reading

- https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase
- https://stackoverflow.com/questions/8939977/git-push-rejected-after-feature-branch-rebase
- https://git-scm.com/docs/git-rebase

### Examples

```bash

# scenario setup
git checkout feature-branch
git commit -m "another one"
git commit -m "money in the bank"

git checkout master
git commit -m "for immediate release"
git commit -m "push directly to production"

# rebase example
git checkout feature-branch
git rebase master

```
