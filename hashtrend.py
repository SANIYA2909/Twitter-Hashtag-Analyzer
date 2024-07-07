import shlex

tweets = ""
tweetCount = input("Enter the number of tweets: ")

while True:
    try:
        tweetCount = int(tweetCount)
        break
    except ValueError:
        tweetCount = input("Please enter a valid number for the tweet count: ")

# Collect tweets
for tweet in range(tweetCount):
    tweets += input(f"Enter tweet {tweet + 1}: ") + "\n"

tweetWords = shlex.split(tweets)
hashTags = [tweetWord for tweetWord in tweetWords if tweetWord.startswith('#')]
hashTagWithCounts = {hashTag: hashTags.count(hashTag) for hashTag in set(hashTags)}
highestCountHashTags = sorted(hashTagWithCounts.items(), key=lambda hashTag: (-hashTag[1], hashTag[0]))
top5HashTags = highestCountHashTags[:5]

print("Top 5 trending hashtags:")
for hashTag, count in top5HashTags:
    print(f"{hashTag}: {count}")
