import urllib.request   # Библиотека для работы с URL
import bs4              # Библиотека BeautifulSoup для парсинга URL

resp = urllib.request.urlopen('https://online.hse.ru/pluginfile.php/604906/question/questiontext/744541/1/789281/task_7_3_2.html')  # Открываем URL
http = resp.read().decode('utf8')   # Читаем страничку

soup = bs4.BeautifulSoup(http, features='html.parser')      # Обрабатываем супом страничку, добавил features='html.parser' (была ошибка)

for link in soup.find_all('a'):     # Находим теги 'a'
    if link.has_attr('href'):       # Проверяем наличие атрибута для ссылки href
        myUrl = link.get('href')
        if myUrl.startswith('https') or myUrl.startswith('http'):
            print(link.get('href'))