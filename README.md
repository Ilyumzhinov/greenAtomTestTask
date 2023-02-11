# Решения для задачек для стажёра

### Задача 1

HTTP ошибка с кодом 500 означает ошибку на стороне сервера.

- Прежде всего нужно проверить логи сервера, связанные с конкрентым API: время, когда произошла ошибка, клиенский IP, метод запроса, URL и параметры запроса.

- Нужно попробовать возпроизвести ошибку, используя инструменты для тестирования HTTP запросов. 

- Затем нужно проверить код, связанный с этим API.

- Наконец можно проверить конфиги сервера или состояние базы данных. 

### Задача 2

Ошибка заключалась в том, что цикл `for` в Python не создаёт отдельного контекста для каждой итерации, из-за чего все лямбда функции ссылаются на одну и ту же переменную `step`, которая после завершения цикла имеет значение 4. Решить проблему можно, создав локальный аргумент лямбда функции и присвоив ему значение `step`.

```python
from typing import Callable

def create_handlers(callback: Callable[[int], None]) -> list[Callable[[int], None]]:
    handlers = []
    for step in range(5):
        # добавляем обработчики для каждого шага (от 0 до 4)
        handlers.append(lambda step=step: callback(step))
    return handlers

def execute_handlers(handlers: list[Callable[[int], None]]) -> None:
    # запускаем добавленные обработчики (шаги от 0 до 4)
    for handler in handlers:
        handler()
```

### Задача 3

```python
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
```

Вывод функции:

```python
Количество тэгов: 774
Количество тэгов с атрибутами: 478
```

### Задача 4

```python
import requests

# Запрос
f = requests.get('http://ipconfig.me')

# Вывод
print(f.text)
```

Вывод функции:

```
38.132.105.156
```

### Задача 5

```python
def compare_versions(A, B):
    # Раздели в подверсии и преврати в числа
    asections = list(map(int, A.split('.')))
    bsections = list(map(int, B.split('.')))

    for i in range(len(max(asections, bsections))):
        a = asections[i] if len(asections) > i else 0
        b = bsections[i] if len(bsections) > i else 0
        # Return -1 if version A is older than version B
        if a < b: return -1
        # Return 1 if version A is newer than version B
        if a > b: return 1
    
    # Return 0 if versions A and B are equivalent
    return 0

A, B = "1.10", "1.1"
print(f'Сравнение версий {A} и {B}: {compare_versions(A, B)}')
```

Вывод функции:

```
Сравнение версий 1.10 и 1.1: 1
```
