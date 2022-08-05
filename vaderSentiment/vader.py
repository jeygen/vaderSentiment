
#from nltk.sentiment.vader import SentimentIntensityAnalyzer
from vaderSentiment import *

sid = SentimentIntensityAnalyzer()
def get_sentiment(sentence):     
	return sid.polarity_scores(sentence)
