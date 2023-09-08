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

git diff ./lib/file.php | patch -p1 ../app-new/lib/file.php
patch -p1 $(git diff ./lib/file_in_git_path.php) ./lib/a_different_file.php
```

## Basic Usage 

```bash
git config --global alias.co checkout
git config --global alias.s status
git config --global aias.df diff
```

## Rebase

Rebasing is another way that a developer can keep a feature branch up-to-date with a parent branch. The way rebase does this is by re-writing all the unique commits on the feature branch, after removing them and writing all of the missing commits from the parent branch back onto the feature branch. This means all of your feature branch's commits will have new commit hashes. On successful rebase, the feature branch will appear to have a cleaner commit history, because the feature branch had been updated in such a way that it could have been created from the parent branch's `HEAD`.

**Example:**

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
## Investigating history

Discovering the change history of a file, `$filepath`, that may not exist

```bash
git log -S $filepath

# Example
$ git log -Sdoc/app/_.ad
```

## Co-Authoring

Add multiple people to commit history.

Source: https://wiki.openstack.org/wiki/GitCommitMessages#Including_external_references

```bash
$ git commit -m "A commit we have made together.
>
>
Co-authored-by: Matthew Walther <mbw@openthc.com>
Co-authored-by: name <name@example.com>
Co-authored-by: another-name <another-name@example.com>"
```

## Publishing a new repository from an existing repository

Prerequisite: Have an existing repository hosted somewhere. We will refer to this at "origin"

Example: `gitlab.com/mashiox/origin.git`

- Step 1: Setup the new git repository, refered to as "downstream"

Example: `github.com/mashiox/down.git`

- Step 2: Add the new remote repository to your local repository's origin

```bash
git remote add downstream github.com/mashiox/down.git
```

- Step 3: Checkout a new branch from the main/master branch on origin

```bash
git checkout -b downstream/main
```

- Step 4: Set the new branch's upsteam to "downsteam". Remember "downsteam" is the reference for our new repository.

```bash
git push --set-upstream downstream downstream/main
```

## Copy files from one branch to another branch

```bash
# Naive approach: https://stackoverflow.com/a/307872
git checkout otherbranch myfile.txt

# Copy source at branch's moment into the file in the current working environment
# https://stackoverflow.com/a/7099164
git show otherbranch:myfile.txt > myfile.txt
```

### Recommended Reading

- https://edoceo.com/sys/git
- https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase
- https://stackoverflow.com/questions/8939977/git-push-rejected-after-feature-branch-rebase
- https://git-scm.com/docs/git-rebase
- https://git.wiki.kernel.org/index.php/CommitMessageConventions

