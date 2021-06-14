from bs4 import BeautifulSoup

xml = open('task_8_8_1_mapcity.osm', 'r', encoding='utf8').read()
soup = BeautifulSoup(xml, 'lxml')

for way in soup.find_all('way'):
    for tags in way('tag'):
        if tags['k'] == 'building':
            all_nd = []
            ans = []
            for nd_ in way('nd'):
                all_nd.append(nd_['ref'])
            if all_nd[0] == all_nd[-1]:
                #print(way['id'])
                #print(*all_nd)
                lt= []
                lonlat = {}
                for nds in all_nd:
                    for nd in soup.find_all('node'):
                        if nd['id'] == nds:
                            lt.append((float(nd['lat']), float(nd['lon'])))
                    lonlat[way['id']] = lt
                for v, k in lonlat.items():
                    ans.append(k)
                print(way['id'])
                print(*ans)
