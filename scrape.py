import tweepy
from pprint import pprint


def get_tweet(query):
   #Authenticate program using api
   #Use users auth keys
   consumer_key = "jLSfYIkrNyp4vCHOYTwfLQX2K"
   consumer_secret = "vYLeUUGojuhkItNKz58FwjwZxOTS5fh4PuTKx2vZOKlU4UziwZ"
   access_token = "825369963775004672-WnMKmuLV3eKRPPtykWYBq1cAStaB8mx"
   access_token_secret = "9PFNd33jxjsWqALXXglhKH6V9KexDTy4vxIyXuSVjwSSn"

   #Authenticate the api
   auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
   auth.set_access_token(access_token, access_token_secret)
   
   #Instantiate tweepy model
   api = tweepy.API(auth)

   #Crawl the recent twitter for items
   x=tweepy.Cursor(api.search, q=query).items(1000)
   #x= tweepy.Cursor(api.search, q='cricket', geocode="-22.9122,-43.2302,1km").pages(1)
   tweets =[]
   for i in x:
      # for y in i:
      #    print(y._json['text'])
      #    print("\n")
      tweets.append(i._json['text'])
   return tweets
         
get_tweet()