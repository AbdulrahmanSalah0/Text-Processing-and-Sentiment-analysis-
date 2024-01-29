from textblob import TextBlob

decide = 1
print(
    "Welcome!, this is an algorithm for sentiment analysis .\nType some words and get a word that describes your sentiment!")

while decide == 1:
    file = open('MyText.txt', 'w')
    user_input = input("Please write something for the algorithm :) : ")
    file.write(user_input)
    file.close()

    with open('MyText.txt', 'r') as f:
        text = f.read()
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

    decide = int(input("If you want to analyze another text enter 1 otherwise enter 0 : "))

else:
    print("\nThx for using our algorithm! ")
