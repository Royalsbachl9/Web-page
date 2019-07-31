import json

tweetFile = open("./tweet_small.json", "r")
# file name . load to get the data from the file as JSON data
tweetData = json.load(tweetFile)

# close the file, its already stored in tweetData
tweetFile.close()
# print the data from one tweet
# tweetData [0] ==> {"id", 123}
# directory["id"] ==> 123

for i in range (len(tweetData)):
    print("text: ", tweetData[i]["text"])
