from bs4 import BeautifulSoup
import requests

# Запрос
f = requests.get('https://greenatom.ru', headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"})

# Парсинг HTML
soup = BeautifulSoup(f.content, "html.parser")

# Сколько HTML-тегов в коде главной страницы сайта [greenatom.ru](greenatom.ru)?
print(f'Количество тэгов: {len(soup.find_all())}')

# Сколько из них содержит атрибуты?
print(f'Количество тэгов с атрибутами: {len(soup.find_all(lambda tag: tag.attrs))}')