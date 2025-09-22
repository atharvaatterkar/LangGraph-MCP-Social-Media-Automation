import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("X_API_KEY")
API_SECRET = os.getenv("X_API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

def post_to_x(content: str):
    try:
        client.create_tweet(text=content)
        print(f"Posted to X: {content}")
        return {"status": "success"}
    except Exception as e:
        print(f"Error posting to X: {e}")
        return {"status": "error", "error": str(e)}
