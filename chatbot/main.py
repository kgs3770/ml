import os
import requests
import random
from dotenv import load_dotenv
from typing import Union
from fastapi import FastAPI, Request

from utils import kospi, openai, langchain

app = FastAPI()

load_dotenv()
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
URL = f'https://api.telegram.org/bot{TOKEN}'

@app.post("/")
async def read_root(request: Request):
    body = await request.json()
    # print(body)
    user_id = body['message']['chat']['id']
    text = body['message']['text']

    if text[0] == '/':
        if text == '/lotto':
            numbers = random.sample(range(1, 46), 6)
            output = str(sorted(numbers))
        elif text == '/kospi':
            output = kospi()
        else:
            output = 'X'
    else:
        #output = openai(OPENAI_API_KEY, text)
        output = langchain(text)

    requests.get(f'{URL}/sendMessage?chat_id={user_id}&text={output}')
    # print(user_id, text)
    return body
