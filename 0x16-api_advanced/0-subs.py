#!/usr/bin/python3
"""queries the Reddit API..."""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    """
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    # Construct the API URL for the subreddit
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

        # Make the API request
        response = requests.get(url, headers=headers)
        data = response.json()

        # Extract the subscriber count
        subscribers = data['data']['subscribers']
        return subscribers
    except (KeyError, ValueError):
        # Invalid subreddit or error in API response
        return 0
