import tweepy
from pprint import pprint
consumer_key = "jLSfYIkrNyp4vCHOYTwfLQX2K"
consumer_secret = "vYLeUUGojuhkItNKz58FwjwZxOTS5fh4PuTKx2vZOKlU4UziwZ"
access_token = "825369963775004672-WnMKmuLV3eKRPPtykWYBq1cAStaB8mx"
access_token_secret = "9PFNd33jxjsWqALXXglhKH6V9KexDTy4vxIyXuSVjwSSn"
#bearer = 'AAAAAAAAAAAAAAAAAAAAAL4lIAEAAAAAxq5gNLRhCIg7Sx30afC0OgtQ73s%3DDZCGCq3YlxXMRywFvyMmbFEjNtnpszAVcVaBwfGxAu5px3bHIV'
# OAUTH_KEYS = {'consumer_key':ckey, 'consumer_secret':csecret,'access_token_key':atoken, 'access_token_secret':asecret}



# auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
# api = tweepy.API(auth)

# cricTweet = tweepy.Cursor(api.search, q='cricket', geocode="-22.9122,-43.2302,1km").items(10)

# for tweet in cricTweet:
#    print (tweet.created_at, tweet.text, tweet.lang)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

x= tweepy.Cursor(api.user_timeline, q='cricket', geocode="-22.9122,-43.2302,1km").pages(1)
pprint(x)