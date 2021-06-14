from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('file:///C:/Users/%D0%9A%D0%BE%D1%81%D1%82%D1%8F/MyProject/1.Python%20%D0%B4%D0%BB%D1%8F%20%D0%B8%D0%B7%D0%B2%D0%BB%D0%B5%D1%87%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%B8%20%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D0%BA%D0%B8%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85(Openedu.ru)/XML%20and%20processing%20geo/Task3/task_8_2_2_map2.html') # скачиваем файл

xml = resp.read().decode('utf8') # считываем содержимое
soup = BeautifulSoup(xml, 'xml') # делаем суп с помощью lxml
cnt = 0
for way in soup.find_all('way'): # идем по всем тэгам way
    cnt += 1 # и просто считаем их количество
print(cnt)
