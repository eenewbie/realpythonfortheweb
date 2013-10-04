import tweepy

consumer_key = "FPO3WxLyOTJyf6qHdmIbQ"
consumer_secret = "jFAgNbYQsHKa3MlpZsaVX6LfD01PAQSEMCyamdQiSo"
access_token = "45669840-iFxR3nt6hZqLHjji49UNRWo8B5BMx697Aqc0aANhN"
access_secret = "pMVp0xGKRtO37X5iemUIu2YpRM6DDEDSJGCL5Q1c"

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

tweets = api.search(q='web2py')

for t in tweets:
	print t.created_at, t.text, "\n"
