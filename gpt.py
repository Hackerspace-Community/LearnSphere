import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
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

    query = f'''
            Provide a learning path for {resdata['subject']} in 
            {resdata['field']}. I have prior knowledge of {knowlst} 
            and can dedicate {resdata['days']} days per week and {'hrs'} 
            hours per day to learning. I prefer learning from {learnlst}. 
            Please include the estimated time to complete the learning 
            path and provide links to the necessary resources.
            

            Additional Requirements:

            1. Format your response using Bootstrap cards for a visually appealing layout.
            2. Ensure that all links have the attribute target="_blank" to open in a new tab.
            
            Please provide your response as HTML code that adheres to these requirements, 
            without the <head> and <body> tags. Avoid providing explanations.
            '''

    query2 = "what is 2+2"
    response = query_chatgpt(query)
    print(response)
    return response