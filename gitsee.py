#!/usr/bin/env python3
from args import args
import tasks

def main():
    #Check to see if account data is already possessed
    if tasks.file_exist() == True:

      #Confirming if username matches current stored data
      the_file_name = tasks.get_file_name()
      confirmed = tasks.confirm_data(args.username, the_file_name)
      
      #If data matches move to tasks, else, need to get/update data
      if confirmed == True:
          pass
      else:
          tasks.get_data(args.username)
    else:
      tasks.get_data(args.username)

    #Tasks run based on option used
    if args.total:
        tasks.find_total(args.username)
    elif args.push:
        tasks.inform()
        tasks.find_push(args.username)
    elif args.pull:
        tasks.inform()
        tasks.find_pull(args.username)
    elif args.star:
        tasks.inform()
        tasks.find_star(args.username)
    elif args.create:
        tasks.inform()
        tasks.find_create(args.username)
    elif args.comment:
        tasks.inform()
        tasks.find_comment(args.username)
    elif args.fork:
        tasks.inform()
        tasks.find_fork(args.username)
    else:
        print("No valid option selected. Use -t, -p, -pl, -s, -cr, -co, or -f")

if __name__ == '__main__':
    main()
