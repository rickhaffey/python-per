import sys  # noqa


def custom_handler(type, value, traceback):
    print("Type: {}".format(type))
    print("Value: {}".format(value))
    print("Traceback: {}".format(traceback))


sys.excepthook = custom_handler

# raise an uncaught exception
1 / 0
