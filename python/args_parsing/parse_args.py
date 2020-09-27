#!/usr/bin/env python

import argparse

args_parser = argparse.ArgumentParser(description='Process user arguments.')

# -------------------------------------------------------------------------
# accept integer arguments after all the options are given.
# nargs='+' implies accept more than one argument
# arguments are saved as a list in the variable args.integers
args_parser.add_argument('integers', type=int, nargs='+', help='an integer')

# -------------------------------------------------------------------------
# accept integer argument after the --sum option
# argument is saved as a variable with the name args.sum
# default=max implies this is an optional argument, and if not given sum will be equal to internal value of max.
args_parser.add_argument('--sum', type=int, default=max)

# -------------------------------------------------------------------------
# accept string argument after the --name option
# argument is saved as a variable with the name args.name
# NO default means the value of args.name will be None if not specified
args_parser.add_argument('--name')

# -------------------------------------------------------------------------
# accept float argument after the --float option
# argument is saved as a variable with the name args.float
# required=True means the option is required
args_parser.add_argument('--float', type=float, required=True)

args = args_parser.parse_args()
# -------------------------------------------------------------------------
print (args)
print (args.integers)
print (args.sum)
print (args.name)
print (args.float)
