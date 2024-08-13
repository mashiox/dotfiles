
alias l="ls --color=auto"
alias ll="ls -la --color=auto"
alias ...="cd ../.."

alias d-c="docker-compose"

# Journal-style date stamp
alias stamp="date +%Y-%j"
alias stampw="echo w$(date +%W)"
alias stampweek="echo week-$(date +%W)"

# Usage: jrnl_week
# Creates a weekly journal entry in PWD
jrnl_week() {
	x="$PWD/$(stamp)-$(stampweek).md"
	touch $x
	echo $x
}
# Usage: jrnl_new ENTRY-TITLE
# Creates a new journal entry in PWD
jrnl_new() {
	x="$PWD/$(stamp)-$1.md"
	touch $x
	echo $x
}

# Command prompt format `[YYYY-DDD]$USER@$HOST:$PWD$`
PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\][\D{%Y-%j}]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '

