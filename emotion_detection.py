import json
import requests

def emotion_detector(text_to_analyze):
    """
    Sends the given text to the IBM Watson Emotion Predict API,
    parses the JSON response, extracts emotion scores, and determines which
    emotion has the highest score (the "dominant" emotion)
    """

    # Endpoint URL for the Emotion Predict service
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    # Header specifying the required model ID for the API to be used
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # JSON payload containing the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Send a POST request to the API with headers and JSON payload
    response = requests.post(url, headers=headers, json=myobj)

    # Parse the response text into a Python dictionary
    formatted_response = json.loads(response.text)

    # Extract the emotion scores dictionary from the nested response structure.
    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    # Track which emotion has the highest score ("dominant emotion").
    dominant_emotion = None
    dominant_score = 0.0

    # Iterate through each emotion score and keep the highest score
    for emotion, score in emotions.items():
        if score > dominant_score:
            dominant_score = score
            dominant_emotion = emotion

    # Return a dictionary of emotions with their scores and the dominant emotion.
    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion
    }