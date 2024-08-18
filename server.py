"""
server.py

This module defines a Flask web application for emotion detection.
It provides two routes:
1. /emotionDetector: Accepts a text parameter and returns the emotional analysis of the text.
2. /: Renders the index page with the HTML form for user input.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_function():
    """
    Handles requests to the /emotionDetector route.
    Processes the 'textToAnalyze' parameter from the request, performs emotion detection,
    and returns a formatted response based on the detected emotions.

    Returns:
        str: A formatted string with the detected emotions and the dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        response_text = "Invalid Input! Please try again."
    else:
        response_text = f"For the given statement, the system response is 'anger': \
                    {response['anger']}, 'disgust': {response['disgust']}, \
                    'fear': {response['fear']}, 'joy': {response['joy']}, \
                    'sadness': {response['sadness']}. The dominant emotion is \
                    {response['dominant_emotion']}."

    return response_text

@app.route("/")
def render_index_page():
    """
    Renders the index page with the HTML form for user input.

    Returns:
        str: The HTML content of the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
