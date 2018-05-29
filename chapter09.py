# # Chapter 09 - Input and Output

# ## Command Line Options

# - at startup, placed in `sys.argv`
#   - first element is name of prog
#   - remaining elements are those provided after the program name

import sys

for (i, arg) in enumerate(sys.argv):
    print("{}: {}".format(i, arg))

# `python3 chapter09.py one two three`    

# >>> 0: chapter09.py
# >>> 1: one
# >>> 2: two
# >>> 3: three    


# use `optparse` for more complicated cmd line processing:
# (see ./sandbox/chapter09optparse.py for details)

# ## Environment Variables

import os

for (k, v) in os.environ.items():
    print("{}: {}".format(k, v))


# >>> COLORFGBG: 12;8
# >>> XPC_FLAGS: 0x0
# >>> LANG: en_US.UTF-8
# >>> SHELL: /bin/zsh
# >>> TERM_PROGRAM_VERSION: 3.1.6
# >>> TERM_PROGRAM: iTerm.app
# >>> COLORTERM: truecolor
# >>> TERM: xterm-256color
# >>> HOME: /Users/rhaffey
# ...

# modify variables as follows:

os.environ["FOO"] = "BAR"

# affects running program and subprocesses

# ## Files and File Objects

# open and create a file:

f = open("./path/to/file", "r")

# file modes
# - 'r': read
# - 'w': write
# - 'a': append

# implicitly translate newline character

# - 'rb', 'wb' => "binary mode" - suppress translation of newline

# - 'r+', 'w+' : in place updates
#   - both input and output
#   - output operations must flush before input
#   - 'w+' truncates length to 0 on open

# - 'U', 'rU' : universal newline support
#   - simplifies cross-platform support for newlines

# bufsize param controls
# - 0 : unbuffered
# - 1 : line buffered
# - -n : system default
# - +n : approx buffer size in bytes


