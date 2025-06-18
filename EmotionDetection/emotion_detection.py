import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    
    if response.status_code == 400:
        return { 'anger': None, 'disgust': None, 'fear': None,
                'joy': None, 'sadness': None, 'dominant_emotion': None
                }

    response.raise_for_status()

    formatted_response = response.json()
    emotions_data = formatted_response['emotionPredictions'][0]['emotion']
    
    emotions = {
        'anger': emotions_data['anger'],
        'disgust': emotions_data['disgust'],
        'fear': emotions_data['fear'],
        'joy': emotions_data['joy'],
        'sadness': emotions_data['sadness'],
        'dominant_emotion': max(emotions_data, key=emotions_data.get)
    }

    return emotions
