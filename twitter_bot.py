#twitter API
#apply for twitter API

# write a Python script to interact with a API


import tweepy #a library to interact with Twitter API
import time
#this is what twitter API uses to authenticate your information of the API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #these are strings
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline() #to access the timeline of your twitter
for tweet in public_tweets:
    print(tweet.text)
    
 user = api.me()
 
 print(user.name)
 print(user.followers_count)
 
 
 #generous Bot to follow back
 
 def limit_handle(cursor):
     while True:
         yield cursor.next()
      except tweepy.RateLimitError:
          time.sleep(1000)
          
 
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
   if follower.name = 'someone name':
       follower.follow()
    print(follower.name)
    
#narcissit bot to love your own tweets

for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break