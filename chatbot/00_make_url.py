import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
URL = f'https://api.telegram.org/bot{TOKEN}'

res = requests.get(URL + '/getupdates')
res_dict = res.json()

user_id = res_dict['result'][0]['message']['from']['id']
text = res_dict['result'][0]['message']['text']
#print(user_id, text)

requests.get(f'{URL}/sendMessage?chat_id={user_id}&text={text}')