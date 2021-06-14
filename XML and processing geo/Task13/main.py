from bs4 import BeautifulSoup

xml = open('task_8_7_3_mapcity.osm', 'r', encoding='utf8').read()
soup = BeautifulSoup(xml, 'lxml')

for way in soup.find_all('way'):
    for tags in way('tag'):
        if tags['k'] == 'building':
            all_nd = []
            for nd_ in way('nd'):
                all_nd.append(nd_['ref'])
            if all_nd[0] == all_nd[-1]:
                print(way['id'])
                print(*all_nd)