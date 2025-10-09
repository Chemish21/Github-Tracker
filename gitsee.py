#!/usr/bin/env python3
from args import args
import tasks

def main():
    
    tasks.get_data(args.username)

    if args.total:
        tasks.find_total(args.username)
    elif args.push:
        tasks.find_push(args.username)
    elif args.pull:
        tasks.find_pull(args.username)
    elif args.star:
        tasks.find_star(args.username)
    elif args.create:
        tasks.find_create(args.username)
    elif args.comment:
        tasks.find_comment(args.username)
    elif args.fork:
        tasks.find_fork(args.username)
    else:
        print("No valid option selected. Use -t, -p, -pl, -s, -cr, -co, or -f")

if __name__ == '__main__':
    main()
