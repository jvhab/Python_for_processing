from bs4 import BeautifulSoup

xml = open('task_8_7_1_mapcity.osm', 'r', encoding='utf8').read()
soup = BeautifulSoup(xml, 'lxml')

i = 0
num_str = []
for node in soup.find_all('node'):
    i += 1
    print(node['id'], node['lat'], node['lon'])
    num_str.append([node['id'], node['lat'], node['lon']])
    if i == 100:
        break
print(len(num_str))