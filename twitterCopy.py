import urllib.request
import json
from textblob import TextBlob
import tweepy

consumer_key = ""
consumer_secret = ""


access_token = ""
access_secret = ""

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)


#query = input("enter trend you want to search\n")

bag_of_tweets = set()
tweets = []
count = 100
epoch = 180
places = api.geo_search(query = "INDIA", granularity = "country")
places_id = places[0].id
print(places_id)

query = 'GET President&place:{}'.format(places_id)

for i in range(epoch):

	assert epoch<=180
	
	public_tweets = api.search(query,lang = 'en',count = count)
	

	
	for j in range(len(public_tweets)):

		tweets.append(public_tweets[j].text)	
		


print(len(tweets))
print(tweets[:5])
'''
print(len(public_tweets))
print(type(public_tweets))

for i in range(len(public_tweets)):
	print(public_tweets[i].text)
	print(len(public_tweets[i].text))
	print("\n------")
'''

'''
SentiWordNet can be used.
WordNet for creation of training Data, then using a classifier to predict!
it might take time.
We will add other tweets into existing training dataset!
'''
