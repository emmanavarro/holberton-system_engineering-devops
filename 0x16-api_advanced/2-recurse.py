#!/usr/bin/python3
"""
    Uses the reddit API for get the all hot posts
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Get the all host posts"""
    if after is None:
        return []

    url = "https://www.reddit.com/r/{}/hot.json?limit=100&after={}".format(
        subreddit, after)
    headers = {'user-agent': 'request'}
    response = requests.get(url, headers=headers,
                            allow_redirects=False)
    if str(response) != "<Response [200]>":
        return None
    r_json = response.json()
    hot_posts = r_json.get("data").get("children")
    after = r_json.get("data").get("after")
    for post in hot_posts:
        hot_list.append(post.get("data").get("title"))
    return hot_list + recurse(subreddit, [], after)
