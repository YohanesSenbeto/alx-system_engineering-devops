#!/usr/bin/python3
"""
queries the Reddit API and returns a list containing the titles
of all hot articles for a given subreddit
"""
import requests

def recurse(subreddit, hot_list=[]):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {}).get('children', [])
        for post in data:
            title = post.get('data', {}).get('title', '')
            hot_list.append(title)
        
        after = response.json().get('data', {}).get('after', None)
        if after:
            return recurse(subreddit, hot_list + recurse(subreddit, hot_list, after))
        else:
            return hot_list
    else:
        return None
