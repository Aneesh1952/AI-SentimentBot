import os
import pandas as pd
from textblob import TextBlob
from flask import Flask, request, jsonify
import zipfile

# Initialize Flask app
app = Flask(__name__)

# Path to the zip file (ensure this file is included in your deployment environment)
zip_path = "IMDB Dataset_csv.zip"

# Extract the zip file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall("IMDB_Dataset_csv")  # Extracts into a folder

# Get the path of the extracted CSV file
csv_file_path = os.path.join("IMDB_Dataset_csv", "IMDB Dataset_csv.csv")  # Update with the actual filename if different

# Load the dataset from the extracted CSV file
df = pd.read_csv(csv_file_path)

# Display the first few rows for debugging (comment out in production)
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


# Flask route to handle chatbot interactions
@app.route('/chat', methods=['POST'])
def chat():
    # Get user input from the POST request
    data = request.json
    user_input = data.get("user_input", "")

    # Generate a chatbot response
    response = chatbot_response(user_input)
    return jsonify({"response": response})


# Flask route to test data loading (optional)
@app.route('/data', methods=['GET'])
def get_data():
    # Return the first 5 rows of the dataset as a JSON response
    return df.head().to_json(orient="records")


if __name__ == "__main__":
    # Bind to the port specified by the environment, default to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
