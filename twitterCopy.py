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
tweets_set = set()
count = 100
epoch = 180
places = api.geo_search(query = "India", granularity = "country")
places_id = places[0].id
print(places_id)
trend = "Chelsea"
#query = 'GET President&place:{}'.format(places_id)
#"truncated":true
query = 'GET {}&place:{}'.format(trend,places_id)
wasted_tweets_count = 0

'''
Tweepy return retweeted tweets as truncated!

Few new tweets can still be trancated.

Both truncated are seen be '...'

'''

for i in range(8):

	assert epoch<=180
	
	public_tweets = api.search(query,lang = 'en',count = 20)     #tweet_mode = extended is giving error while truncated = False is not working!
	
	#print(dir(public_tweets[0]))        # to get all functions of this object!!!
	
	for j in range(len(public_tweets)):
		#print(public_tweets[j].truncated)
		#print(public_tweets[j].user.url)
		print("*********************************")
		if(public_tweets[j].truncated==False):
			tweets.append(public_tweets[j].text)	     # to save only complete tweets
			tweets_set.add(public_tweets[j].text)
		else:
			wasted_tweets_count += 1
		


print("Fetched tweets are: ",len(tweets))
print("Wasted tweets from fetched: ",wasted_tweets_count)

i = 1
for i in range(len(tweets_set)):
	print(tweets_set.pop())
	print("\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/")
print("final tweets o/p : ",i+1)
'''
for tweet in tweets:
	print(tweet)
	print("*******")
'''

#print(tweets[:5])
'''
print(len(public_tweets))
print(type(public_tweets))

for i in range(len(public_tweets)):
	print(public_tweets[i].text)
	print(len(public_tweets[i].text))
	print("\n------")
'''