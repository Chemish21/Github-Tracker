#Python
import os
import json
import requests
import sys
import re

def inform():
  print("Listed New to Old")
  print("-----------------")

def file_exist():
  #Confirm if file exists
  return os.path.exists("gh-data.json")

def confirm_data(username: str, name_in_file: str):
  #Confirm username matches username in file repo
  return username == name_in_file
  
def get_name_in_file():
  #Extracts username from first half of repo path
  with open("gh-data.json") as json_file:
    json_data = json.load(json_file)
    for data in json_data:
      the_repo = data["repo"]
      repo_name = the_repo["name"]
      break
    match_name = re.match(r"([^/]+)", repo_name)
    if match_name:
      file_name = match_name.group(1)
    return file_name

def get_data(username: str):
    #Gets/Posts account data and checks if user exists and recent user activity
    request = requests.get(f"https://api.github.com/users/{username}/events")
    if request.status_code == 404:
      print("User does not exist")
      sys.exit()
    else:
      with open("gh-data.json", "w") as json_file:
            request_data = request.json()
            if not request_data:
              print("No recent user activity")
              sys.exit()            
            json.dump(request_data, json_file, indent=2)

def find_total(username: str):
  #Finds totals of account activity
  with open("gh-data.json", "r") as json_file:
    push_count = 0
    pull_count = 0
    star_count = 0
    create_count = 0
    comment_count = 0
    fork_count = 0
    json_data = json.load(json_file)
    for data in json_data:
      if data["type"] == "PushEvent":
        push_count += 1
      if data["type"] == "PullRequestEvent":
        pull_count += 1
      if data["type"] == "WatchEvent":
        star_count += 1      
      if data["type"] == "CreateEvent":
        create_count += 1
      if data["type"] == "IssueCommentEvent":
        comment_count += 1
      if data["type"] == "ForkEvent":
        fork_count += 1
    print(f"{username} pushes: {push_count}")
    print(f"{username} pulls: {pull_count}")
    print(f"{username} stars: {star_count}")
    print(f"{username} creates: {create_count}")
    print(f"{username} comments: {comment_count}")
    print(f"{username} forks: {fork_count}")

def find_push(username: str):
    #Finds all recent account pushes
    with open("gh-data.json", "r") as json_file:
      push_count = 0
      json_data = json.load(json_file)
      for data in json_data:
        if data["type"] == "PushEvent":
          push_count += 1
          the_actor = data["actor"]
          actor_name = the_actor["login"]
          the_repo = data["repo"]
          repo_name = the_repo["name"]
          print(f"Push #{push_count}")
          print(f"{actor_name} pushed to repo: {repo_name}")
          print()

def find_pull(username: str):
  #Finds all recent account pulls
  pull_count = 0
  with open("gh-data.json", "r") as json_file:
    json_data = json.load(json_file)
    for data in json_data:
      if data["type"] == "PullRequestEvent":
        pull_count += 1
        the_actor = data["actor"]
        actor_name = the_actor["login"]
        the_repo = data["repo"]
        repo_name = the_repo["name"]
        print(f"Pull #{pull_count}")
        print(f"{actor_name} pulled from repo: {repo_name}")
        print()

def find_star(username: str):
  #Finds all recent account stars
  star_count = 0
  with open("gh-data.json", "r") as json_file:
    json_data = json.load(json_file)
    for data in json_data:
      if data["type"] == "WatchEvent":
        star_count += 1
        the_actor = data["actor"]
        actor_name = the_actor["login"]
        the_repo = data["repo"]
        repo_name = the_repo["name"]
        print(f"Star #{star_count}")
        print(f"{actor_name} starred repo: {repo_name}")
        print()

def find_create(username: str):
  #Finds all recent account creates
  create_count = 0
  with open("gh-data.json", "r") as json_file:
    json_data = json.load(json_file)
    for data in json_data:
      if data["type"] == "CreateEvent":
        create_count += 1
        the_actor = data["actor"]
        actor_name = the_actor["login"]
        the_repo = data["repo"]
        repo_name = the_repo["name"]
        print(f"Create #{create_count}")
        print(f"{actor_name} created repo: {repo_name}")
        print()

def find_comment(username: str):
  #Finds all recent account comments
  comment_count = 0
  with open("gh-data.json", "r") as json_file:
    json_data = json.load(json_file)
    for data in json_data:
      if data["type"] == "IssueCommentEvent":
        comment_count += 1
        the_actor = data["actor"]
        actor_name = the_actor["login"]
        the_repo = data["repo"]
        repo_name = the_repo["name"]
        print(f"Comment #{comment_count}")
        print(f"{actor_name} commented repo: {repo_name}")
        print()

def find_fork(username: str):
  #Finds all recent account forks
  fork_count = 0
  with open("gh-data.json", "r") as json_file:
    json_data = json.load(json_file)
    for data in json_data:
      if data["type"] == "ForkEvent":
        fork_count += 1
        the_actor = data["actor"]
        actor_name = the_actor["login"]
        the_repo = data["repo"]
        repo_name = the_repo["name"]
        print(f"Fork #{fork_count}")
        print(f"{actor_name} forked repo: {repo_name}")
        print()
