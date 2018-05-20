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

# RESUME @ Importing Selected Symbols from a Module
