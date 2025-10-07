#Python
import os
import json
import requests
import sys

def get_data(username: str):
    request = requests.get(f"https://api.github.com/users/{username}/events")
    if request.status_code == 404:
      print("User does not exist")
      sys.exit()
    if not os.path.exists("gh-data.json"):
        with open("gh-data.json", "w") as json_file:
            request_data = request.json()
            if not request_data:
              print("No recent user activity")
              sys.exit()
            json.dump(request_data, json_file, indent=2)
    else:
        with open("gh-data.json", "w") as json_file:
            request_data = request.json()
            if not request_data:
              print("No recent user activity")
              sys.exit()            
            json.dump(request_data, json_file, indent=2)

def find_total(username: str):
  with open("gh-data.json", "r") as json_file:
    push_count = 0
    pull_count = 0
    star_count = 0
    create_count = 0
    comment_count = 0
    fork_count = 0
    json_data = json.load(json_file)
    if not json_data:
      print("No recent user activity or user does not exist")
      return
    else:
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
    print(f"Total {username} pushes: {push_count}")
    print(f"Total {username} pulls: {pull_count}")
    print(f"Total {username} stars: {star_count}")
    print(f"Total {username} creates: {create_count}")
    print(f"Total {username} comments: {comment_count}")
    print(f"Total {username} forks: {fork_count}")

def find_push(username: str):
    with open("gh-data.json", "r") as json_file:
      push_count = 0
      json_data = json.load(json_file)
      if not json_data:
        print("No recent user activity or user does not exist")
        return
      for data in json_data:
        if data["type"] == "PushEvent":
          push_count += 1
          the_actor = data["actor"]
          actor_name = the_actor["login"]
          the_repo = data["repo"]
          repo_name = the_repo["name"]
          print(f"Push #{push_count}")
          print(f"{actor_name} pushed to {username}'s repo: {repo_name}")
          print("------------------------------------")

def find_pull(username: str):
  pull_count = 0
  with open("gh-data.json", "r") as json_file:
    json_data = json.load(json_file)
    if not json_data:
      print("No recent user activity or user does not exist")
      return
    for data in json_data:
      if data["type"] == "PullRequestEvent":
        pull_count += 1
        the_actor = data["actor"]
        actor_name = the_actor["login"]
        the_repo = data["repo"]
        repo_name = the_repo["name"]
        print(f"Pull #{pull_count}")
        print(f"{actor_name} pulled from {username}'s repo: {repo_name}")
        print("------------------------------------")

def find_star(username: str):
  star_count = 0
  with open("gh-data.json", "r") as json_file:
    json_data = json.load(json_file)
    if not json_data:
      print("No recent user activity or user does not exist")
      return
    for data in json_data:
      if data["type"] == "WatchEvent":
        star_count += 1
        the_actor = data["actor"]
        actor_name = the_actor["login"]
        the_repo = data["repo"]
        repo_name = the_repo["name"]
        print(f"Star #{star_count}")
        print(f"{actor_name} starred {username}'s repo: {repo_name}")
        print("------------------------------------")

def find_create(username: str):
  create_count = 0
  with open("gh-data.json", "r") as json_file:
    json_data = json.load(json_file)
    if not json_data:
      print("No recent user activity or user does not exist")
      return
    for data in json_data:
      if data["type"] == "CreateEvent":
        create_count += 1
        the_actor = data["actor"]
        actor_name = the_actor["login"]
        the_repo = data["repo"]
        repo_name = the_repo["name"]
        print(f"Create #{create_count}")
        print(f"{actor_name} created with {username}'s repo: {repo_name}")
        print("------------------------------------")

def find_comment(username: str):
  comment_count = 0
  with open("gh-data.json", "r") as json_file:
    json_data = json.load(json_file)
    if not json_data:
      print("No recent user activity or user does not exist")
      return
    for data in json_data:
      if data["type"] == "IssueCommentEvent":
        comment_count += 1
        the_actor = data["actor"]
        actor_name = the_actor["login"]
        the_repo = data["repo"]
        repo_name = the_repo["name"]
        print(f"Comment #{comment_count}")
        print(f"{actor_name} commented regarding {username}'s repo: {repo_name}")
        print("------------------------------------")

def find_fork(username: str):
  fork_count = 0
  with open("gh-data.json", "r") as json_file:
    json_data = json.load(json_file)
    if not json_data:
      print("No recent user activity or user does not exist")
      return
    for data in json_data:
      if data["type"] == "ForkEvent":
        fork_count += 1
        the_actor = data["actor"]
        actor_name = the_actor["login"]
        the_repo = data["repo"]
        repo_name = the_repo["name"]
        print(f"Fork #{fork_count}")
        print(f"{actor_name} forked {username}'s repo: {repo_name}")
        print("------------------------------------")
