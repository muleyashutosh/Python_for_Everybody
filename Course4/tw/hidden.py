from dotenv import load_dotenv
import os
load_dotenv()

def oauth():

    consumer_key = os.getenv('Twitter_consumer_key')
    consumer_secret = os.getenv('Twitter_consumer_secret')
    token_key = os.getenv('Twitter_token_key')
    token_secret = os.getenv('Twitter_token_secret')

    return {"consumer_key": consumer_key,
            "consumer_secret": consumer_secret,
            "token_key": token_key,
            "token_secret": token_secret}
