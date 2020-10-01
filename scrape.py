import tweepy                             #Module used to retrieve tweets
from pprint import pprint                 #Module used for clarity behind prints
from geopy.geocoders import Nominatim     #Module used to turn location into geoCoordinates


def get_geoCode(location):
    location = geolocator.geocode(location)
    location= (location.latitude, location.longitude)
    return location

def get_tweet(query,location=None):
    #Instantiate tweepy model
    api = tweepy.API(auth)
    
    #Gather and retrieve tweets based upon only query
    if not location:
        tweets=tweepy.Cursor(api.search, q=query).items(1000)
        outputOfTweets =[]
        for tweet in tweets:
            outputOfTweets.append(tweet._json['text'])
        return outputOfTweets
        
    #get the geo data
    geo = get_geoCode(location)
    print(geo[0])
    geo = "{},{},1km".format(geo[0],geo[1])
    #Crawl the recent twitter for tweets
    print(geo)
    tweets=tweepy.Cursor(api.search, q=query,geocode=geo).items(1000)
    outputOfTweets =[]
    for tweet in tweets:
        outputOfTweets.append(tweet._json['text'])
    return outputOfTweets

if __name__ == "__main__":
    #Authenticate program using api
    #Use users auth keys
    consumer_key = "jLSfYIkrNyp4vCHOYTwfLQX2K"
    consumer_secret = "vYLeUUGojuhkItNKz58FwjwZxOTS5fh4PuTKx2vZOKlU4UziwZ"
    access_token = "825369963775004672-WnMKmuLV3eKRPPtykWYBq1cAStaB8mx"
    access_token_secret = "9PFNd33jxjsWqALXXglhKH6V9KexDTy4vxIyXuSVjwSSn"

    #Authenticate the api
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    #Authenticate the geolocater
    geolocator = Nominatim(user_agent="globalSearch")

    ### GET USER INPUT ###
    
    query = input("What Topic would you like to scrape: ")
    location = input("Would you like to gather data from a certain location (Y/N): ")
    if location.lower() == "y":
        print("Where would you like to gather data from:")
        print("For example 'Hyderabad', or 'London' or even a specific address like: ")
        print("1A Survey No: 62, Bahadurpally, Hyderabad, Telangana 500043? \n")
        location = input("Please enter: ") 
    else:
        location= None
    #start the model
    pprint(get_tweet(query, location))
