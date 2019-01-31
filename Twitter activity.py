#!/usr/bin/env python
# coding: utf-8

# # Social Media Activity (Twitter)
# 
# ## User details
# consumer_key : aZqxfmKH5E2arKCdpgZsVe3E1
# consumer_secret : kmNenKC6aHz4HqP3eLSI2aXCDRopGZYz6Aui2K5VupKIwKQl4M
# 
# access_token : 622232148-xs7brb0jEmSrr1R1HAJHTxroJQmUWzJnvB7MLg3F
# access_secret : aQn5vdOzeziT6tOQlc8tRnAMHN4SCoMuvDjIshNMsLsM0

# In[37]:


# Import the necessary libraries
import tweepy
from tweepy import OAuthHandler
import numpy as np

# Authenticate tweepy
consumer_key = 'aZqxfmKH5E2arKCdpgZsVe3E1'
consumer_secret = 'kmNenKC6aHz4HqP3eLSI2aXCDRopGZYz6Aui2K5VupKIwKQl4M'

access_token = '622232148-xs7brb0jEmSrr1R1HAJHTxroJQmUWzJnvB7MLg3F'
access_secret = 'aQn5vdOzeziT6tOQlc8tRnAMHN4SCoMuvDjIshNMsLsM0'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# Get the tweets for the wanted topic (#Scotland) and create a list to store them (ediTweet)
topic = '#Scotland'
editTweet = list(tweepy.Cursor(api.search, q = topic).items(10))

# Initialise empty lists for the attribute data and the counters
locations = []
followers = []
above_100_fol = 0
below_100_fol = 0

# Loop through the tweets and append the data to the relevant lists and counters
for tweet in editTweet:
    locations.append(tweet.user.location)
    followers.append(tweet.user.followers_count)
    if tweet.user.followers_count > 100: above_100_fol += 1
    if tweet.user.followers_count < 100: below_100_fol += 1
    
# Print the required results
print ('1: The users that tweeted something about {} are from the following locations: {}'.format (topic, locations))
print ('2: All users have {} followers on average'.format(int(np.mean(followers))))
print ('3: {} users have more than 100 followers'.format(above_100_fol))
print ('4: {} users have less than 10 followers'.format(below_100_fol))

