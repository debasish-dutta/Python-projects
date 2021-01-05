import auth_key
import tweepy
import time

auth = tweepy.OAuthHandler(auth_key.API_key, auth_key.API_secret_key)
auth.set_access_token(auth_key.Access_token, auth_key.Access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()

def tweet():
    message = input("Enter your tweet: ")
    try:
        api.update_status(message)
        print("Tweet updated")
    except tweepy.TweepError as e:
        print(e.reason)

if __name__ == "__main__":
    tweet()