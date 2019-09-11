#
#   welcome, battle cat
#
#       it's been a while since we've seen each other . .
#
#

import tweepy
import random
import time
from keys import *

# IMPORTANT TWITTER STUFF

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)
# OK THAT'S IT


msg = "What's your favorite Blueberry song?"

# keywords
kwd = ['ice cream', 'found a rock' , 'peeling' , 'headwater', 'dogface', 'blue river', "cross game", "gainer" ]

# start the first tweet
tweet = api.update_status(status = msg)

# scan for a reply
while True:
    time.sleep(20)
    mentions = api.mentions_timeline(count=1,since_id=tweet.id)

    for mention in mentions:
        if kwd[0] in mention.text.lower():
            status = (""" %s Sleep in a little longer, four weeks 'til the end of the summer... i'm feeling weird. 
            The sun was spilling thru the blinds and you were smiling in the light...""" % tweet.id)
            tweet = api.update_status(status=status, in_reply_to_status_id=tweet.id)
            break
        elif kwd[1] in mention.text.lower():
            status = ("""I found a rock... on the front porch... it was formed in the shape of a heart... picked it up and i held it... let it hang from the cracks in my fingers...""")
            tweet = api.update_status(status=status, in_reply_to_status_id=mention.id_str)
            break
        elif kwd[2] in mention.text.lower():
            status = ("""You're too close to notice all of the good things about yourself. i've been patiently waiting, hoping you see them on your own. Do you still stick your nose up when they ask how i'm doing??""")
            tweet = api.update_status(status=status, in_reply_to_status_id=mention.id_str)
            break
        elif kwd[3] in mention.text.lower():
            status = ("""I need to calm down...do you feel the fire underground? It melts my feet and sparks the spaces in between...""")
            tweet = api.update_status(status=status, in_reply_to_status_id=mention.id_str)
            break
        elif kwd[4] in mention.text.lower():
            status = ("<3")
            tweet = api.update_status(status=status, in_reply_to_status_id=mention.id_str)
            break
        elif kwd[5] in mention.text.lower():
            status = ("""%s All the words that i say, sound so dumb coming out of my mouth...Wish i could tell you what's been troubling me but i'm afraid, of what you'll think...""")
            tweet = api.update_status(status=status, in_reply_to_status_id=mention.id_str)
            break
        elif kwd[6] in mention.text.lower():
            status = ("""Built a chair from my bed to the window...Candle lights flicker shapes across the wall...Not a sound except the whisper of your breathing...Gentle heart, growing softer...""")
            tweet = api.update_status(status=status, in_reply_to_status_id=mention.id_str)
            break
        elif kwd[7] in mention.text.lower():
            status = """We're breathing flowers... In the dead lands..."""
            tweet = api.update_status(status=status, in_reply_to_status_id=mention.id_str)
            break

        else:
            status = ("i wish :( pick a song thats recorded.")
            tweet = api.update_status(status=status, in_reply_to_status_id=mention.id_str)
            break
