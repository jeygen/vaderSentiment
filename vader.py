
#from nltk.sentiment.vader import SentimentIntensityAnalyzer
import vaderSentiment as vs 
sid = vs.SentimentIntensityAnalyzer()
def get_sentiment(sentence):     
	return sid.polarity_scores(sentence)
print(get_sentiment("hello chap you suck"))

