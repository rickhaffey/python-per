import optparse

p = optparse.OptionParser()

p.add_option("-d", "--data", dest="data_path",
             help="retrieve input data from DATA")

p.add_option("-l", "--log", action="store_true", dest="log", help="write output to log")

p.set_defaults(log=False)

opts, args = p.parse_args()

print("data_path: {}".format(opts.data_path))
print("log: {}".format(opts.log))
print("remaining args: {}".format(args))


# `python3 sandbox/ch09optparse.py -d /Users/rhaffey/demo -l foo bar`

# >>> data_path: /Users/rhaffey/demo
# >>> log: True
# >>> remaining args: ['foo', 'bar']


# help is provided automatically via `-h`

# `python3 sandbox/ch09optparse.py -h`

# >>> Usage: ch09optparse.py [options]
# >>> 
# >>> Options:
# >>>   -h, --help            show this help message and exit
# >>>   -d DATA_PATH, --data=DATA_PATH
# >>>                         retrieve input data from DATA
# >>>   -l, --log             write output to log
