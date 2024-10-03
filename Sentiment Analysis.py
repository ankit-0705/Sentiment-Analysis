#Importing libraries for sentiment analysis
from textblob import TextBlob
import re
import json
valid_limit = 0
limit = 0

#Extracting the data from the json file
file_path = "C:\\Users\\Ankit Sangwan\\OneDrive\\Desktop\\study material\\Python\\tweets python sentiment analysis.json"

with open(file_path,'r') as file:
    data = json.load(file)

tweet_texts = [entry['tweet_text'] for key,entry in data.items() if 'tweet_text' in entry]

#Limiting the extraction of data upto n times
while valid_limit<1:
    limit = input("Enter the limit of analysis: ")
    if limit.isdigit():
        valid_limit+=1
    else:
        continue

limited_tweet = tweet_texts[:int(limit)]

for user_text in limited_tweet:

    # Removing everything other than characters and words
    def clean_text(text):
        c_text = re.sub(r'[^\s\w]', "", text)
        return c_text
    outcome = clean_text(user_text)


    # Removing web_url and phone_numbers
    def remove_web_num(text):
        w_text = re.sub(r'http\S+|www\S+|https\S+', "", text, flags=re.MULTILINE)
        num_text = re.sub(r'\d+', "", w_text)
        return num_text
    final_outcome = remove_web_num(outcome)


    # Shortening the original tweet
    def short_tweet(sentence, n):
        short_w = sentence.split()
        n_words = short_w[:n]
        return ' '.join(n_words)
    short_sentence = short_tweet(user_text, 7)
    print(f"Tweet: {short_sentence}.......")

    # Doing sentiment analysis
    blob = TextBlob(final_outcome)
    result = blob.sentiment
    if result.polarity > 0:
        if result.subjectivity > 0.5:
            print("The review is Positive and Personal opinion-oriented.")
        elif result.subjectivity == 0.5:
            print("The review is Positive but it is Neutral in subjectivity.")
        else:
            print("The review is Positive and Data-driven.")
    elif result.polarity == 0:
        if result.subjectivity > 0.5:
            print("The review is Neutral in polarity but it is Personal opinion-oriented.")
        elif result.subjectivity == 0.5:
            print("The review is Neutral in polarity as well as subjectivity.")
        else:
            print("The review is Neutral in polarity but it is Data-driven.")
    elif result.polarity < 0:
        if result.subjectivity > 0.5:
            print("The review is Negative and Personal opinion-oriented.")
        elif result.subjectivity == 0.5:
            print("The review is Negative but it is Neutral in subjectivity.")
        else:
            print("The review is Negative and Data-driven.")
    else:
        print("Unknown Error Occurred!!!")

    print("Stats:", result)
    print("---------------------------------------------------------------------")
    print()