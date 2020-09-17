#!/usr/bin/python3
"""
    Uses the reddit API to print the number of subscribers of a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Get the numbers of subscribers by subreddit given"""
    url_rsubs = "https://api.reddit.com/r/{}/about".format(subreddit)
    headers = {'User-Agent': 'Python3'}
    response = requests.get(url_rsubs, headers=headers,
                            allow_redirects=False)
    if str(response) != "<Response [200]>":
        return 0
    r_json = response.json()
    subs_count = r_json.get('data').get('subscribers')
    return subs_count
