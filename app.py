import pandas as pd
from textblob import TextBlob
import zipfile
import os

# Path to the zip file
zip_path = "IMDB Dataset_csv.zip"

# Extract the zip file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall("IMDB_Dataset_csv")  # Extracts into a folder

# Get the path of the extracted CSV file
csv_file_path = os.path.join("IMDB_Dataset_csv", "IMDB Dataset_csv.csv")  # Update with the actual filename if different

# Load the dataset from the extracted CSV file
df = pd.read_csv(csv_file_path)

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
user_inputs = [
    "I love this product! It's amazing.",
    "I'm not happy with the service.",
    "It's okay, nothing special."
]

for user_input in user_inputs:
    response = chatbot_response(user_input)
    print(f"User  Input: {user_input}")
    print(f"Chatbot Response: {response}")
