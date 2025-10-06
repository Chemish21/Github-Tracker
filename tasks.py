#Python
import os
import json
import requests

def get_data(username: str):
  request = requests.get(f"https://api.github.com/users/{username}/events")
  if not os.path.exists("gh-data.json"):
    with open("gh-data.json", "w") as json_file:
      request_data = request.json()
      json.dump(request_data, json_file, indent=2)
  else:
    with open("gh-data.json", "w") as json_file:
      request_data = request.json()
      json.dump(request_data, json_file, indent=2)

def find_events(username: str):
    with open("gh-data.json", "r") as json_file:
      push_count = 0
      pull_count = 0
      create_count = 0
      star_count = 0
      comment_count = 0
      fork_count = 0
      json_data = json.load(json_file)
      for data in json_data:
        if data["type"] == "PushEvent":
          push_count = push_count + 1
        if data["type"] == "PullRequestEvent":
          pull_count = pull_count + 1
        if data["type"] == "CreateEvent":
          create_count = create_count + 1
        if data["type"] == "WatchEvent":
          star_count = star_count + 1
        if data["type"] == "IssueCommentEvent":
          comment_count = comment_count + 1
        if data["type"] == "ForkEvent":
          fork_count = fork_count + 1
      print(f"{username}'s recent Pushes: {push_count}")
      print(f"{username}'s recent Pulls: {pull_count}")
      print(f"{username}'s recent Creations: {create_count}")
      print(f"{username}'s recent Stars: {star_count}")
      print(f"{username}'s recent Comments: {comment_count}")
      print(f"{username}'s recent Forks: {fork_count}")
