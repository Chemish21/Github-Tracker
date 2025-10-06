#Python
import argparse

#Implementing top level parsers
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

#Implementing subparser
name_parser = subparsers.add_parser("name")

#username parser
name_parser.add_argument("username", type=str, help="enter username of github account")

#Finalizing parser
args = parser.parse_args()
