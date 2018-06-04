# # Chapter 10 - Execution Environment

# * output of commands in interactive mode uses `repr()`
# * can override by using `sys.displayhook`

# result of last operation stored in `_` variable
# - assignment happens within `sys.displayhook`

# ## Site Module

# - imported automatically to configure third-party modules and packages
# - adds additional directories to the module search path
#   - can use path configuration files (`.pth`) to specify addition of
#     other modules and packages
# - additional `sitecustomize` module

# ## Per-User Site Packages

# - ~/.local/lib/python3.6/site-packages
# - Anaconda uses this to manage environments

# ## Enable Future Features

# `from __future__ import {feature}`
# - should appear as first stmt of module

# ## Program Termination

# terminates when:
# - no more statements
# - uncaught `SystemExit` exception raised
# - interpreter receives `SIGTERM` or `SIGHUP`

# cleanup of objects via `__del__` isn't guaranteed
# some approaches to handle:

# - register a cleanup method

import atexit, gc

def cleanup():
    # do any cleanup work here...

    # call the garbage collector?
    gc.collect()
    pass

atexit.register(cleanup)

# - `NameError` may be generated if `__del__` method attempts to
# access already destroyed global data

# it's possible to terminate _without_ performing cleanup actions via:
# `os._exit(status)`


