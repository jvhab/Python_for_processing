from bs4 import BeautifulSoup

xml = open('task_8_4_1_map2.osm', 'r', encoding='utf8').read()
soup = BeautifulSoup(xml, 'lxml')
i = 0
for node in soup.find_all('node'):
    for tag in node('tag'):
        if tag['k'] == 'amenity' and tag['v'] == 'fuel':
            i += 1
print(i)