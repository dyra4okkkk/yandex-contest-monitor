import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

COOKIE = os.getenv('YANDEX_COOKIE', '')
START_ID = int(os.getenv('START_ID', 94000))
END_ID = int(os.getenv('END_ID', 97000))
MAX_WORKERS = int(os.getenv('MAX_WORKERS', 15))

HEADERS = {
    'Cookie': COOKIE,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}
SEARCH_PATTERNS = ["АиСД", "2026"]#Пример