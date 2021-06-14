from bs4 import BeautifulSoup

xml = open('task_8_4_2_map2.osm', 'r', encoding='utf8').read()
soup = BeautifulSoup(xml, 'lxml')

i_1 = 0
i_2 = 0
for node in soup.find_all('node'):
    for tag in node('tag'):
        if tag['k'] == 'amenity' and tag['v'] == 'fuel':
            i_1 += 1

for way in soup.find_all('way'):
    for tag2 in way('tag'):
        if tag2['k'] == 'amenity' and tag2['v'] == 'fuel':
            i_2 += 1
print(i_1 + i_2)