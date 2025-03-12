import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
NGROK_URL = os.getenv('NGROK_URL')

URL = f'https://api.telegram.org/bot{TOKEN}/setWebhook'

# print(TOKEN)
# print(NGROK_URL)
print(f'{URL}?url={NGROK_URL}')