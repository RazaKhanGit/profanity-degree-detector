import re
from tkinter.constants import SEPARATOR

f = open('words.txt', 'r')
profaneWords = [tweet.rstrip('\n') for tweet in f] #reading from the tweetlist, and removing the trailing '\n'

def tokenize(text): #tokenizing the input text
    list = [tweet.lower() for tweet in re.split(r'[`\-=~!@#$%^&*()_+\[\]{} ;\'\\:"|<,./<>?]', text)]
    return list

fTweets = open('tweet.txt', 'r')
tweets = [tweet.rstrip('\n') for tweet in fTweets]
tweetTokenized = [tokenize(t) for t in tweets]
with open('profaneDegree.txt', 'w') as f:
    for i in range(len(tweets)):
        n = 0
        for w in tweetTokenized[i]:
            if w in profaneWords:
                n = n + 1
            else:
                for pw in profaneWords:
                    if w.find(pw) != -1:
                        n = n+1

        
        degree_of_profanity = n/len(tweetTokenized[i])
        f.write(tweets[i]+ ":"+ str(round(degree_of_profanity, 3))+"\n")