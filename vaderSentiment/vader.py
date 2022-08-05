
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()
def get_sentiment(sentence):     
	return sid.polarity_scores(sentence)
