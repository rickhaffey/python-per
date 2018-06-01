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

# additional parameters to open:

# - encoding: e.g. 'utf-8', 'ascii', etc.
# - errors: error-policy to use for encoding errors
# - newline: behavior of universal newline mode
# - closefd: close file descriptor on close()? (default: True)

# ### File object methods

# open for writing
f = open("demo", "w")

# write some lines
f.write("line one\n")
f.writelines(["line two\n", "line three\n", "line four\n", "line five\n", "end\n"])
f.close()

# open for reading
f = open("demo", "r")

f.read() # return the entire file contents
# >>> 'line one\nline two\nline three\nline four\nline five\nend\n'
f.seek(0) # reset position at start of file 
f.read(4) # >>> 'line'
f.seek(0)
f.readline()  # >>> 'line one\n'
f.tell()   # >>> 9
f.readline()  # >>> 'line two\n'
f.seek(9)
f.readline(3)  # >>> 'lin'
f.seek(9)
f.readline(30)  # >>> 'line two\n'
f.readlines() # >>> ['line three\n', 'line four\n', 'line five\n', 'end\n']

# read and readline indicate EOF via an empty string:
f.seek(0)
while True:
    line = f.readline()
    if not line:
        break

f.seek(0)
for line in f:
    print(line)

# read methods return Unicode or byte strings depending on
# whether file was opened in text or binary mode

# `.tell()` returns the file pointer of the current byte offset
# `.seek(n)` moves the file pointer to a given byte offset
#   adding a `whence` parameter indicates the 'reference' point of the offset
#   - 0 : start of file
#   - 1 : relative to current position
#   - 2 : relative to the end of the file

# file attributes:
# - .closed
# - .name
# - .mode
# - .newlines
# - .encoding

# ## Standard Input, Output, and Error

# 3 standard file objects provided by `sys` module:
# - sys.stdin
# - sys.stdout
# - sys.stderr

import sys
sys.stdout.write("Enter your name: ")
name = sys.stdin.readline().strip()
print("Name: {}".format(name))

# short-cut using `input`
# - print prompt
# - accept response
# - strip newline
name = input("Enter your name: ")
print("Name: {}".format(name))

# sys.stdout, stdin, and stderr can be replaced
# with alternate file objects to re-direct their
# input / output

# ## The `print` Function

# `print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`
print("one", "two", "three")  # >>> one two three\n
print("one", "two", "three", sep=",") # >>> one,two,three\n
print("one", "two", "three", end="<<<") # >>> one two three<<<


print("one", end="")
print("two", end="")
print("three", end="")

# >>> onetwothree

# Print objects to the text stream file, separated by sep and followed by end. sep, end, file and
# flush, if present, must be given as keyword arguments.

# 
# All non-keyword arguments are converted to strings like str() does and written to the stream,
# separated by sep and followed by end. Both sep and end must be strings; they can also be None,
# which means to use the default values. If no objects are given, print() will just write end.
# 
# The file argument must be an object with a write(string) method; if it is not present or None,
# sys.stdout will be used. Since printed arguments are converted to text strings, print() cannot be
# used with binary mode file objects. For these, use file.write(...) instead.
# 
# Whether output is buffered is usually determined by file, but if the flush keyword argument is
# true, the stream is forcibly flushed.
# 
# Changed in version 3.3: Added the flush keyword argument.

# ## Variable Interpolation in Text Output

# - no built-in $ type variable interpolation
# - 3 alternate approaches

# %-formatting
t = "this is %(name)s number %(number)d"
print(t % { "name": "example", "number": 1 })

# `.format` method
t = "this is {name} number {number}"
print(t.format(name="example", number=1))

# templates
import string
t = string.Template("this is $name number $number")
print(t.substitute({ "name": "example", "number": 1 }))


# ## Generating Output

# a generator function can be used to produce output incrementally
# and buffer the transmittal of that output to some I/O destination
# - done using the `yield` keyword

def generate(n):
    while n > 0:
        yield "value: {}".format(n)
        n -= 1

# write to a file        
f = open("output", "w")
f.writelines(generate(10))

# iterate over
for line in generate(10):
    print(line)

# collect all at once
lines = list(generate(10))

# ## Unicode String Handling

# [ ] TODO: use the p3 docs to summarize this

# ## Object Persistence and the `pickle` Module

# - the pickle module serializes an object into a stream of bytes that can be
#   written to a file and later restored

class Foo:
    def __init__(self, bar, bat):
        self.bar = bar
        self.bat = bat

    def display(self):
        print("Foo")
        print("\tbar: {}".format(self.bar))
        print("\tbat: {}".format(self.bat))

foo = Foo("this is BAR", "this is BAT")

import pickle

# write out pickled object
f = open("foo", "wb")
pickle.dump(foo, f)
f.close()

# read in pickled object
f = open("foo", "rb")
foo2 = pickle.load(f)
f.close()

foo2.display()

# >>> Foo
# >>> 	bar: this is BAR
# >>> 	bat: this is BAT

# `shelve` is similar to pickle, but stores pickled objects in a
#  dictionary like structure

# - pickle data format is python specific
# - multiple storage protocols over history of python versions
#   - 0 : oldest
#   - 1 & 2 : newer, more efficient binary formats
# - protocol can be specified in dump call
# - protocol need not be specified in load - it's encoded in the
#   pickled object representation

# `__getstate__()` and `__setstate__()` methods are used to
# allow writing / reading custom state as part of pickling
# e.g.: getstate could save the filepath of a contained file object,
#   and setstate could re-load that file upon un-pickling
    

