#!/usr/bin/env python3
from args import args
import tasks

def main():
  if args.command == 'name':
    tasks.get_data(args.username)
    tasks.find_events(args.username)

if __name__ == '__main__':
  main()
