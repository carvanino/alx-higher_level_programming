#!/usr/bin/python3
"""
List the most recent commit of a repository given the username and
repository name
"""
import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    user_name = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
            user_name, repo_name)
    r = requests.get(url)
    try:
        r_dict = r.json()
        r_dict = r_dict[:10]
        for commit in r_dict:
            print("{}: {}".format(
                commit['sha'], commit['commit']['author']['name']))
    except KeyError:
        pass
