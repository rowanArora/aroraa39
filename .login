# $Header: /admin/cvsroot/cdf/local.share/cdf/skel/.login,v 1.7 2020/04/24 22:10:47 agenkin Exp $
# Default .login script for CSC students
# Run once, when you log in.

# Establish the terminal settings. This sets your backspace key to "control-H"
# (equivalent to the backspace key on a workstation keyboard), and your
# interrupt key to "control-C". See the manual page for stty for more info.

tty -s && stty -tabs erase "^H" intr "^C"

# set default file permissions to prevent read, write or execute by 
# anybody other than yourself. Don't change this, or somebody may be able
# to read and copy your assignments. 
umask 077
  
# prevent people from "talk"ing or "write"ing to your terminal. Change this
# to "mesg y" if you want to allow this.
tty -s && mesg n
