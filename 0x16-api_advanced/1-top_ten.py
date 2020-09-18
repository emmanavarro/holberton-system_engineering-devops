#!/usr/bin/python3
"""
    Uses the reddit API for get the 10 hot posts
"""
import requests


def top_ten(subreddit):
    """Get the 10 host posts"""
    url_sred = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    url_sred += "?limit=10"
    headers = {'user-agent': 'request'}
    response = requests.get(url_sred_inf, headers=headers,
                            allow_redirects=False)
    if str(response) != "<Response [200]>":
        print(None)
        return
    r_json = response.json()
    hot_posts_json = r_json.get("data").get("children")
    top10_posts = ''
    for post in hot_posts_json:
        top10_posts += post.get("data").get("title") + '\n'
    print(top10_posts, end='')
