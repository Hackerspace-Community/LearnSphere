import requests
import json

API_KEY = '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'
API_URL = 'https://api.openai.com/v1/chat/completions'

def query_chatgpt(query):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }

    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': query}]
    }

    response = requests.post(API_URL, headers=headers, json=data)
    response_data = response.json()
    print(response_data)

    return response_data['choices'][0]['message']['content']

def query(resdata):
    # data = json.loads(resdata)
    print(type(resdata))
    # lst=[]
    # for keys,values in resdata.items():
    #     if keys not in ['knowledge','learn']:
    #         lst.append(values)

    knowlst=" and ".join(resdata['knowledge'])
    learnlst=" and ".join(resdata['learn'])
    # print(lst)
    #give me a learning path for ai in computer science i know python java i can give 
    # 6 -7 days in a week and 2-4 hrs a day and i can learn from video audio and
    #  book and also say how much time it will take along with links

    query = f"Give me a learning path in json format for {resdata['subject']} in {resdata['field']} i know {knowlst} i can give {resdata['days']} in a week and {'hrs'} per day i prefer learning from {learnlst} also tell me how much time it will take to complete and provide the links too."
    print(query)
    response = query_chatgpt(query)
    return response