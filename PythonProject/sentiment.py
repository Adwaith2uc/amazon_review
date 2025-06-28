from textblob import TextBlob

# Step 1: Take input
text = input("Enter a sentence to analyze: ")

# Step 2: Create a TextBlob object
blob = TextBlob(text)

# Step 3: Perform sentiment analysis
sentiment = blob.sentiment

# Step 4: Print results
print("\nSentiment Analysis Result:")
print(f"Polarity (–1 to 1): {sentiment.polarity}")
print(f"Subjectivity (0 to 1): {sentiment.subjectivity}")

# Step 5: Interpret polarity
if sentiment.polarity > 0:
    print("Overall Sentiment: Positive 😊")
elif sentiment.polarity < 0:
    print("Overall Sentiment: Negative 😠")
else:
    print("Overall Sentiment: Neutral 😐")
