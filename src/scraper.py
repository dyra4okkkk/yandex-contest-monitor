import logging
import requests
from typing import List
from src.config import HEADERS, SEARCH_PATTERNS

session = requests.Session()
session.headers.update(HEADERS)

def extract_title(html: str) -> str:
    """Извлекает заголовок страницы без тяжелого BeautifulSoup."""
    if "<title>" in html and "</title>" in html:
        return html.split("<title>")[1].split("</title>")[0]
    return "Название не определено"

def check_id(contest_id: int) -> None:
    """Проверяет наличие целевого контеста по заданному ID."""
    urls: List[str] = [
        f'https://official.contest.yandex.ru/contest/{contest_id}/enter',
        f'https://contest.yandex.ru/contest/{contest_id}/enter'
    ]
    
    for url in urls:
        try:
            response = session.get(url, timeout=4)
            response.raise_for_status() 
            html = response.text
            
            if "Зарегистрироваться" in html: #"Register" if english
                continue
            
            if all(pattern in html for pattern in SEARCH_PATTERNS):
                title = extract_title(html)
                logging.info(f"MATCH FOUND! ID: {contest_id} | Title: {title} | URL: {url}")
                break 
                
        except requests.RequestException:
            pass