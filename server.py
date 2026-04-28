"""
Flask server for the Emotion Detection web application.
"""
from flask import Flask,  render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """Render the index page."""
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detector_endpoint():
    """
    Reads the 'textToAnalyze' query string parameter, calls emotion_detector(),
    and returns the formatted response.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    # Call the application function from the package and format the output
    output = emotion_detector(text_to_analyze)
    formatted_output = (
        "For the given statement, the system response is "
        f"'anger': {output['anger']}, 'disgust': {output['disgust']}, 'fear': {output['fear']}, "
        f"'joy': {output['joy']} and 'sadness': {output['sadness']}." 
        f"The dominant emotion is <b>{output['dominant_emotion']}</b>."
    )

    # Return the formatted output
    return formatted_output


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
