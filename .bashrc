# $Header: /admin/cvsroot/cdf/local.share/cdf/skel/.bashrc,v 1.11 2021/02/24 16:50:38 norman Exp $
# Default .bashrc file for CSC students whose login shell is Bash.
# This file is executed whenever a new shell is started (eg. when a
# new (xterm) window is created).

# A "PATH" is a list of directories in which the system looks for commands.
# This path puts a "bin" subdirectory in your home directory first, so that
# you can have your own versions of commands override the default versions,
# if you want. The other directories include the X-Window programs
# (in /local/bin/X11), the CDF-specific (local) programs (in /local/bin),
# programs that originally came from the University of California at Berkeley
# (/usr/ucb), and other general programs (/usr/bin).
#
# The dot (.) at the end of the path allows commands in the current directory
# to be run. Make sure this is at the end of your path.
#
# Feel free to change these, but make sure that you have /usr/ucb, /usr/bin, 
# /bin, and /local/bin in your path, and that /local/bin preceeds the other 
# three.

export PATH=$HOME/bin/${OSTYPE}:$HOME/bin:/local/bin/X11:/local/bin:/bin:/usr/bin

# Interactive shell prompt.
PS1='\h:\w\$ '

# set useful variables. EDITOR is your default line editor, VISUAL is
# the default visual (full-screen) editor. Other good choices for VISUAL
# could be /usr/bin/jove or /usr/bin/emacs.
export EDITOR=ed
export VISUAL=vi

# make it harder to wipe out files
set -o noclobber

# checks for mail every five minutes
MAIL=/var/spool/mail/$USER
MAILCHECK=300

# some aliases to force an "are you sure?" if action might result in data loss.
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# alias to allow use of "p" as a pager. Eg. "ls /local/bin | p"
alias p='more -s -d'

umask 077

# Change the window title of X terminals 
case $TERM in
        xterm*|rxvt|eterm)
                PROMPT_COMMAND='echo -ne "\033]0;${USER}@${HOSTNAME%%.*}:${PWD/$HOME/~}\007"'
                ;;
        screen)
                PROMPT_COMMAND='echo -ne "\033_${USER}@${HOSTNAME%%.*}:${PWD/$HOME/~}\033\\"'
                ;;
esac

