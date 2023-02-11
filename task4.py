import requests

# Запрос
f = requests.get('http://ipconfig.me')

# Вывод
print(f.text)