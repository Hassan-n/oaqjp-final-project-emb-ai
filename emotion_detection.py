import requests

def emotion_detector(text_to_analyze):
    """
    Sends the given text to the IBM Watson Emotion Predict API and returns
    the raw response containing detected emotions.
    """

    # Endpoint URL for the Emotion Predict service
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    # Header specifying the required model ID for the API to be used
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # JSON payload containing the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Send a POST request to the API with headers and JSON payload
    response = requests.post(url, headers=headers, json=myobj)
    
    # Return the raw response text from the API
    return response.text