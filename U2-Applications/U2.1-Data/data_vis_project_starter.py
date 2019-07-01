'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

def avg(lst):
    return sum(lst)/len(lst)



#Get the JSON data
tweetFile = open("TwitterData/tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below! 
tweettext = []
tweetstring = ""
for tweet in tweetData:
    tweetstring += tweet["text"]
    #blob = TextBlob(tweet['text'])
    #tweettext.append(blob)


#my_list = [1,2,3,4,5,6] 
#print(sum(my_list)/len(my_list))

tweetBlob = TextBlob(tweetstring)

blob_poplarity = []
for blob in tweettext:
    blob_polarity.append(blob.polarity)

blob_subjectivity = []
for blob in tweettext:
    blob_subjectivity.append(blob_subjectivity)

word_dict = {}

for word in tweetBlob.words:
    word_dict[word.lower()] = tweetBlob.word_counts[word.lower()]

print(word_dict)

#blob_polarity.sort()
#print(blob_polarity)

# Textblob sample:
tb = TextBlob("You are a horrible computer scientist.")
