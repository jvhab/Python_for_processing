from bs4 import BeautifulSoup

xml = open('task_8_3_2_map2.osm', 'r', encoding='utf8').read()
soup = BeautifulSoup(xml, 'lxml')
all_way = []
for node in soup.find_all('way'):
    nd_1 = 0
    id_way = node['id']
    for nd in node('nd'):
        nd_1 += 1
    all_way.append([id_way, nd_1])

my_sort = sorted(all_way, key=lambda x: x[1], reverse=True)
print(my_sort)