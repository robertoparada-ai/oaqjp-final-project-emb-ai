import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    response = requests.post(url, json=myobj, headers=headers)
    
    # Convertir el texto de respuesta a un diccionario
    formatted_response = json.loads(response.text)
    
    # Extraer las emociones
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Crear el diccionario con el formato requerido
    result = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness']
    }
    
    # Encontrar la emoción dominante (la de mayor puntaje)
    dominant_emotion = max(result, key=result.get)
    result['dominant_emotion'] = dominant_emotion
    
    return result