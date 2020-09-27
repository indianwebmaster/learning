# !/usr/bin/env python
# While parse_args.py is a better option if using python 3.x, if using 2.x you can still use getopt to parse arguments with relative ease.
# In this case, the burden of int/string/float and required/optional validation is on the programmer, and not as easy as in parse_args.py

import getopt
import sys

user_args = {}


def usage():
    print (sys.argv[0] + " [-h] [--sum intval] [--name strval] [--float float_val] intval1 [intval2 ...]")


def parse_args(args):
    try:
        optlist, optargs = getopt.getopt(args, 'h', ['sum=', 'name=', 'float='])
    except getopt.GetoptError as err:
        print (str(err))
        usage()
        sys.exit(2)

    for opt in optlist:
        if opt[0] == '-h':
            usage()
            sys.exit(0)

        # Enter opt/val in dict. Remove -- from the opt
        user_args[opt[0][2:]] = opt[1]

    if (len(optargs)) > 0:
        user_args["args"] = optargs
    else:
        print ("At least one intval1 is required")
        usage()
        sys.exit(2)


# Use this example to test
args = '--sum 10 --name john --float 100.0 300 400'.split()
# args = sys.argv[1:]
parse_args(args)
for opt, val in user_args.items():
    print (opt, val)
