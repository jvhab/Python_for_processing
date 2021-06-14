from bs4 import BeautifulSoup

xml = open('task_8_2_3_map2.osm', 'r', encoding='utf8').read()
soup = BeautifulSoup(xml, 'lxml')
i = 0
for node in soup.find_all('node'):
    i += 1
print(i)
