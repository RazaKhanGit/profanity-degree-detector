# profanity-degree-detector

### Assumptions:
1. Defined degree of profanity as **(#ofProfaneWords) / (#ofTotalWords)** in a sentence
1. All the profane words in [wordsList.txt](/wordsList.txt) is having **same** degree of profanity
2. Capitalizing of Word doesnot increase the profanity

### How to use:
1. Add profane words or slurs to monitor in [wordsList.txt](/wordsList.txt)
2. Add tweets in [tweetList.txt](/tweetList.txt) to check for degree of profanity
3. Run the script [main.py](/main.py), it will create a .txt file with tweets and their degree of profanity

used [this](https://github.com/ben174/profanity/blob/master/profanity/data/wordlist.txt) dataset for [wordsList.txt](/wordsList.txt) and [this](https://github.com/amoudgl/short-jokes-dataset/blob/master/shortjokes.csv) for [tweetList.txt](tweetList.txt)
