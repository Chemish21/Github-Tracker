#Python
import argparse

#Top-level parser
parser = argparse.ArgumentParser(description="Get GitHub user activity")

#Positional argument for username
parser.add_argument("username", type=str, help="GitHub username")

#Optional flags
parser.add_argument("-t", "--total", action="store_true", help="Get total action count")
parser.add_argument("-p", "--push", action="store_true", help="Get all recent pushes")
parser.add_argument("-pl", "--pull", action="store_true", help="Get all recent pull requests")
parser.add_argument("-s", "--star", action="store_true", help="Get all recent stars")
parser.add_argument("-cr", "--create", action="store_true", help="Get all recent creates")
parser.add_argument("-co", "--comment", action="store_true", help="Get all recent comments")
parser.add_argument("-f", "--fork", action="store_true", help="Get all recent forks")

#Parse arguments
args = parser.parse_args()
