from bs4 import BeautifulSoup

xml = open('task_8_3_1_map2.osm', 'r', encoding='utf8')
soup = BeautifulSoup(xml, 'lxml')

ALL_TAG = 0
ALL_NODE = 0

for node in soup.find_all('node'):
    ALL_NODE +=1
    for tag in node('tag'):
        ALL_TAG += 1
print(ALL_NODE - ALL_TAG, ALL_TAG)
