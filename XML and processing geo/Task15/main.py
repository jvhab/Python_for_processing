from bs4 import BeautifulSoup
import math

xml = open('task_8_8_2_mapcity.osm', 'r', encoding='utf8').read()
soup = BeautifulSoup(xml, 'lxml')


def getsqr(coordlist):
    baselat = coordlist[0][0]
    baselon = coordlist[0][1]
    degreelen = 111300
    newcoord = []
    for now in coordlist:
        newcoord.append(((now[0] - baselat) * degreelen, (now[1] - baselon) * degreelen * math.sin(baselat)))
    sqr = 0
    for i in range(len(newcoord) - 1):
        sqr += newcoord[i][0] * newcoord[i + 1][1] - newcoord[i + 1][0] * newcoord[i][1]
    sqr += newcoord[-1][0] * newcoord[0][1] - newcoord[0][0] * newcoord[-1][1]
    return abs(sqr)

finish = []
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
                finish.append((getsqr(*ans), way['id']))
                #print(way['id'])
                #print(*ans)
my_sort = sorted(finish, key=lambda x: x[0], reverse=True)
print(my_sort)



