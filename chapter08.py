# # Chapter 08 - Modules, Pakcages, and Distribution

# ## Modules and the `import` Statement

# - any python file can be used as a module
# - load via `import {filename - no extension}`

# When loading via import (first time):
# - creates a namespace - a container for the objects defined in file
#   - corresponds to `global` within the context of those objects
# - executes module's code within this new namespace
# - creates a name within the _caller_ that corresponds to this
#     new namespace

# multiple modules can be imported via comma separated list:
import os, re, random

# modules can be "aliased"
import re as regex

# modules are first-class objects in Python
# - can be assigned to variables,
# - placed in data structures,
# - passed around as data

# `import` can appear at any point in a program

# dictionary containing all currently loaded modules
import sys
sys.modules


# ## Importing Selected Symbols from a Module

# `from` used to load specific definitions from within a module
# places references to one or more of the objects defined in the
# module in the caller's namesapce

from re import match
from re import match, search
from re import (match,
                search,
                split)

# allows aliasing

from re import match as mtch

# `*` loads all defs except those that start with `_`
# - note, this can only be used at the top level of a module
#   i.e., it can't be used within function bodies, etc.

from re import *

# the imported module can control what definitions are imported
# via `from m import *` using `__all__`:

# module: foo.py
__all__ = ['bar', 'bat', 'baz']

# importing defs using `from` still imports the defs into
# the `global` namespace of the imported module, not `global`
# of the caller
# - references to global variables within the imported definitions
#   refer to those variables within the imported module's namespace,
#   not the _caller's_ namespace.

# ## Execution as the Main Program

# two ways in which a python source file can execute:
# - via `import` as a library module
# - directly as the main program or script

# each modules defines a `__name__` variable:
# - the name of the top-level module of the interpreter is `__main__`
# - this is commonly used to alter a module's behavior depending on
#   whether it's loaded as a module or run as a script:

if __name__ == "__main__":
    # do something when run as a program
    pass
else:
    # do something else when loaded as a module
    pass

# ## The Module Search Path

# - interpreter searches list of dirs in `sys.path`
# - search path follows order of directories listed
# - zip files can be included in list of paths
#   - .py, .pyw, .pyc, and .pyo files only
#   - .pyc and .pyo files won't be created when .py files are loaded from zip
# - sub-dirs within zip files can be included in list
# - .egg files can be included in list

# ## Module Loading and Compilation

# 4 types of modules loaded with `import`:
# - .py files
# - C / C++ extensions in shared libs or DLLs
# - python packages
# - builtin modules (written in C, linked into interpreter)

# File search order for `import foo` within each directory in the search path:
# note: search is case sensitive to match module name in `import` stmt
# 1. a directory, `foo`, defining a package
# 2. `foo.pyd`, `foo.so`, `foomodule.so`, or `foomodule.dll` (compiled extensions)
# 3. `foo.pyo` (if `-O` or `-OO` option used)
# 4. `foo.pyc`
# 5. `foo.py`

# for option #5 (`.py`), at first import, the file is compiled to byte code,
# generating a `.pyc` file; subsequent imports load this file unless the
# timestamp on the source `.py` file is newer
# `-B` : prevents generation of `.pyc` files
# if `.pyc` or `.pyo` files present, `.py` not necessary to run
# `.pyc` files are Python version specific, may not work with different release

# `.pyo` files generated via the interpreters `-O` and `-OO` options:
# `-O`: stripped of line numbers, assertions, and debugging info
# `-OO`: like `-O`, but also strips documentation strings

# ## Module Reloading and Unloading

# - no safe way to reload or unload modules that have been imported
# - main recourse is to re-start the python interpreter process

# ## Packages

# - allows grouping a collection of modules under a shared name
# - defined by
#   - 1. creating a directory with same name as package
#   - 2. creating an `__init__.py` file within that directory
#   - 3. placing module files within that directory
# - can contain 'sub-packages'

# RESUME @ ## Packages
