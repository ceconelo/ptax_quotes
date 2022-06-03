#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import tweepy
from configparser import RawConfigParser
from datetime import datetime

config_parser = RawConfigParser()
config_parser.read(os.path.join(os.path.dirname(__file__), '../settings.ini'))
credentials = config_parser['credentials']


'''
    This module is responsible for requests to the twitter API through the tweetpy library.
    There are 3 main functions:
    1. Create an object with read and write permissions on twitter
    2. Search recent tweets
    3. Post new tweets in sequential mode 
'''


# Object with permissions to consume the Twitter API.
def get_client():
    # According to the library documentation we need a project created
    # on the twitter platform. In this project we get the keys and tokens needed for the connection.
    client = tweepy.Client(bearer_token=credentials['bearer_token'],
                           access_token=credentials['access_token'],
                           access_token_secret=credentials['access_token_secret'],
                           consumer_key=credentials['api_key'],
                           consumer_secret=credentials['api_key_secret'],
                           wait_on_rate_limit=False)
    return client


# Search recent tweets
def search_tweets(client, query, max_results):
    start = datetime.today().strftime('%Y-%m-%dT') + '03:00:00Z'
    tweets = client.search_recent_tweets(query=query, max_results=max_results, start_time=start)
    tweet_data = tweets.data
    results = []
    if not tweet_data is None and len(tweet_data) > 0:
        for tweet in tweet_data:
            results.append({
                'id': tweet.id,
                'text': tweet.text
            })
    return results


def get_tweet(client, id):
    tweet = client.get_tweet(id, expansions=['author_id'], user_fields=['username'])
    return tweet


# Method with the main objective of creating the connection object, making the search call of the
# tweets and returning a list of the tweets.
def search_tweet_list(query, max_results):
    # Object of connection
    client = get_client()
    # Searching for tweets
    tweets = search_tweets(client, query, max_results)
    # Creating list of tweets
    objs = []
    if len(tweets) > 0:
        for tweet in tweets:
            twt = get_tweet(client, tweet['id'])
            objs.append({
                'text': tweet['text'],
                'username': twt.includes['users'][0].username,
                'id': tweet['id'],
                'url': 'https://twitter.com/{}/status/{}'.format(twt.includes['users'][0].username, tweet['id'])
            })
    return objs, client


# Method responsible for posting the tweets
def tweet_to_publish(text, query):
    # Before posting we check if we already have tweets for that query
    # today
    tweets, client = search_tweet_list(query, 10)
    if tweets:
        # if we already have tweeted about it today we create a sequential post
        # For this to happen we get the id of the tweet we want to follow
        return client.create_tweet(text=text, in_reply_to_tweet_id=tweets[0]['id'])
    else:
        # if there are no posts on the day we create a new post
        return client.create_tweet(text=text)
