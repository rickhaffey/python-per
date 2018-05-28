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

# import statement with packages:
# - `import level1.level2.level3.foo`
#   - imports module `foo`
#   - all calls to methods within foo must be prefixed with `level1.level2.level3.foo.`
# - `from level1.level2.level3 import foo`
#   - imports module `foo`
#   - allows calling methods in `foo` with `foo.` prefix
# - `from level1.level2.level3.foo import method1`
#   - loads foo but only imports `method1`, which can be called directly

# at first import of any package, all code in `__init__.py` is executed

# import *:
# - `from level1.level2.level3 import *`
#    - will only import the names defined in the `__all__` list within `__init__.py`

# within another module in the same package:
# - e.g. with level1.level2.level3.bar:
#   `from level1.level2.level3 import foo`
#   OR
#   `from . import foo`
# - !note: for relative packages, don't use `import foo`
#   - python will look in std lib
#   - if not present, error
#   - if there _is_ a module with that name, it will load _that_
#     rather than the desired, sibling module
# - to load from another level directory in the same package
#   - `from ..level2 import baz`
# - relative imports
#   - can only use the `from {module} import {symbol}` form
#   - symbol must be a valid identifier
#   - can only refer to other symbols within the same package hierarchy

# importing a pkg name alone doesn't automatically import all submodules
# but, if the __init__.py file(s) in those packages have relative
# imports of the contained modules, then the bare package import will
# indirectly import those modules as a result of the code in `__init__.py`
# running

# during package import, python defines a `__path__` variable available
# within `__init__.py` containing the list of directories to search
# when looking for a pkg
# - initially set with an entry to the containing directory of the package
# - `__init__.py` can add additional search directories if needed

# ## Distributing Python Programs And Libraries

# - use `distutils` module
# - create a directory containing
#   - packages, modules
#   - scripts
#   - documentation (including README)
# - organize code so it runs via `python` from the top level directory
# - create files `setup.py` with code similar to

from distutils.core import setup

setup(
    name="{package name}",
    version="{version}",
    py_modules=['{module1}', '{module2}', 'etc.'],
    packages = ['{package1}', '{package2}', 'etc.'],
    scripts = ['{script1}', 'etc.']
)

# - additional parameters can be applied to method
# - run `python3 setup.py sdist` to create a source distribution
#   - will create an archive file in the `dist` subdirectory
#   - file can be distributed to others for installation
#   - to install, unzip file, then run `python setup.py install`
#   - installs package to local distribution:
#     - packages to `site-packages`
#     - scripts to the directory of the python interpreter
# - during install, process will rewrite python shebang line
#   to match location of local python install
# - `python setup.py bdist` will build a binary distribution

# to create a setuptools .egg file, adjust setup as follows:

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name="foo", ...)

# ## Installing Third-Party Libraries

# typically installed to `site-packages`
# to install in a per-user library, use `python setup.py install --user`
# to install to custom location: `python setup.py install --prefix {path}`
# setuptools includes an `easy_install` to streamline install process
# `python setup.py register` to register to PyPI
    


