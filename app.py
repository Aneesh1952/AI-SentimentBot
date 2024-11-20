import pandas as pd
from textblob import TextBlob

# Load the dataset from a local file
df = pd.read_csv(r"IMDB Dataset_csv.xls")  # Make sure the file is in the same directory or provide the full path

# Display the first few rows
print(df.head())

# Define a function to analyze sentiment
def analyze_sentiment(text):
    analysis = TextBlob(text)
    # Classify sentiment as positive, negative, or neutral
    if analysis.sentiment.polarity > 0:
        return "positive"
    elif analysis.sentiment.polarity < 0:
        return "negative"
    else:
        return "neutral"

# Example chatbot responses based on sentiment
def chatbot_response(user_input):
    sentiment = analyze_sentiment(user_input)
    if sentiment == "positive":
        return "I'm glad to hear that! How can I assist you further?"
    elif sentiment == "negative":
        return "I'm sorry to hear that. How can I make things better for you?"
    else:
        return "Thank you for sharing your thoughts. How can I help you today?"

# Test the chatbot response
user_input = "I love this product! It's amazing."
response = chatbot_response(user_input)
print(f"User  Input: {user_input}")
print(f"Chatbot Response: {response}")

user_input = "I'm not happy with the service."
response = chatbot_response(user_input)
print(f"User  Input: {user_input}")
print(f"Chatbot Response: {response}")

user_input = "It's okay, nothing special."
response = chatbot_response(user_input)
print(f"User  Input: {user_input}")
print(f"Chatbot Response: {response}")
