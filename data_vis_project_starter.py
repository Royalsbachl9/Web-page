
'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
#Get the JSON data
tweetFile = open("./tweet_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!

# Textblob sample:
polarity = []
subjectivity = []
for i in range(len(tweetData)):
    tb = TextBlob(tweetData[i]["text"])
    print("polarity:", tb.polarity)
    print("subjectivity:", tb.subjectivity)
    polarity.append(tb.polarity)
    subjectivity.append(tb.subjectivity)
# print(polarity)
total = 0
for i in polarity:
    total = total + i
average = total/len(polarity)
print(average)

for i in subjectivity:
    total = total + i
average = total/len(subjectivity)
print(average)

num_bins = 6
n, bins, patches = plt.hist(polarity, num_bins, facecolor = 'pink', alpha = 0.3)
plt.show()

num_bins = 6
n, bins, patches = plt.hist(subjectivity, num_bins, facecolor = 'pink', alpha = 0.3)
plt.show()


alltweets = []
for i in range(len(tweetData)):
    tweets = alltweets.append(tweetData[i]["text"])


# filter out most frequnce used words using directory

TextBlob.word
# textblob.words_count{}
# key: word
# value: frequnce
#
# felteredDict = {}
# key:words
# value : frequnce
