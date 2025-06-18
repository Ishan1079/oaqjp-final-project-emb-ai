"""Flask web server for emotion detection using IBM Watson NLP API."""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def get_emotion():
    """
    Handle GET request for emotion detection.

    Returns a formatted string containing emotion scores and dominant emotion.
    If input is missing or emotion cannot be determined, returns an error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze:
        return "Invalid text! Please try again!"

    response = emotion_detector(text_to_analyze)

    return (
            f"For the given statement, the system detected the following emotions: "
            f"Anger: {response['anger']}, "
            f"Disgust: {response['disgust']}, "
            f"Fear: {response['fear']}, "
            f"Joy: {response['joy']}, "
            f"Sadness: {response['sadness']}. "
            f"The dominant emotion is {response['dominant_emotion']}."
        )

@app.route("/")
def render_index_page():
    """
    Render the main index HTML page.

    Returns the rendered HTML template.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
