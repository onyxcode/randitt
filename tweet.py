import tweepy
import json
import requests
from dotenv import load_dotenv as env
from os import getenv
env()

API_KEY = getenv('API_KEY')
API_SECRET = getenv('API_SECRET')
BEARER_TOKEN = getenv('BEARER_TOKEN')
ACCESS_TOKEN = getenv('ACCESS_TOKEN')
ACCESS_SECRET = getenv('ACCESS_SECRET')

auth = tweepy.OAuthHandler(API_KEY, API_SECRET) 
  
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET) 
api = tweepy.API(auth)

twt = input("What's happening?\n> ")
api.update_status(status=twt)