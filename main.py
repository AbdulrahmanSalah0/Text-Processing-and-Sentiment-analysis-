from textblob import TextBlob
from newspaper import Article

url = 'https://en.wikipedia.org/wiki/Negative_feedback'
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.text
print(text)
blob = TextBlob(text)
user_sentiment = blob.sentiment.polarity

if user_sentiment <= -0.8:
    print("Terrible")
elif user_sentiment <= -0.5:
    print("Very bad")
elif user_sentiment < 0:
    print("Bad")
elif user_sentiment == 0:
    print("Neutral")
elif user_sentiment <= 0.5:
    print("Good")
elif user_sentiment <= 0.8:
    print("Very good")
else:
    print("Amazed")

print(user_sentiment)
