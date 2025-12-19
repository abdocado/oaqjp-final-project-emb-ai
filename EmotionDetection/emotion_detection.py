import requests
def emotion_detector(text):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text } }
    response = requests.post(url, json = obj, headers=header)
    json_response = response.json()
    my_item = json_response["emotionPredictions"][0]["emotion"]
    max_val = max(my_item, key=my_item.get)
    if response.status_code == 400:
        
        final_response = {"anger":None,
                        "disgust":None,
                        "fear":None,
                        "joy":None,
                        "sadness":None,
                        "dominant_emotion":None
                        }
        return final_response
    else:
        final_response = {"anger":my_item["anger"],
                        "disgust":my_item["disgust"],
                        "fear":my_item["fear"],
                        "joy":my_item["joy"],
                        "sadness":my_item["sadness"],
                        "dominant_emotion":max_val
                        }
    
        return final_response


