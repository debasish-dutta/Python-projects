import auth_key
import tweepy
import time

auth = tweepy.OAuthHandler(auth_key.API_key, auth_key.API_secret_key)
auth.set_access_token(auth_key.Access_token, auth_key.Access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

indId = 2282863
india_trend = api.trends_place(indId)
tweetNo = 5
a =[]

trndInd = api.trends_place(indId)

for trend in trndInd[0]['trends']:
    a.append(trend['name'])

for item in a:
    print(item)
    for tweet in tweepy.Cursor(api.search, item).items(tweetNo):
        try:
            print("tweet liked & retweeted")
            tweet.favorite()
            tweet.retweet()
            time.sleep(10)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
