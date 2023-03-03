# import urllib library
from urllib.request import urlopen
  
# import json
import json

# store the URL in url as parameter for urlopen
url = "https://mihaicf.github.io/jsontest/tweets.json"
  
# store the response of URL
response = urlopen(url)
  
# storing the JSON response from url in data
data_json = json.loads(response.read())
#print(len(data_json))

# Search for tweets with #FlixBus
tweet_selection = [tw for tw in data_json if '#FlixBus' in tw['text']]
for index in range(0, len(tweet_selection)):

    # Date time of the tweet
    created_at = tweet_selection[index]['created_at']
    print(created_at)

    # Hashtags
    hashtags = tweet_selection[index]['entities']['hashtags']
    for val in hashtags:
        hashtags_text = val['text']
        print(hashtags_text)

    # Is it a retweet?
    retweeted_status = tweet_selection[index].get("retweeted_status")
    if retweeted_status != None:
        print("Retweet: YES") 
    else:
        print("Retweet: NO")
    
    # Number of followers
    followers_count = tweet_selection[index]['user']['followers_count']
    print("Number of followers:", followers_count)

    # Location
    location = tweet_selection[index]['user']['location']
    print("Location:", location)
    print()
    



