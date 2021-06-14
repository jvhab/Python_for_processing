import bs4
import urllib.request

response = urllib.request.urlopen('file:///C:/Users/%D0%9A%D0%BE%D1%81%D1%82%D1%8F/MyProject/HTML/task10/Moscow%20-%20Wikipedia.html')
myhtml = response.read().decode('utf8')

soup = bs4.BeautifulSoup(myhtml, 'html.parser')
all_link_list = []
all_link_list_new = []
all_link_set = set()

for link in soup.find_all('a'):
    if link.has_attr('href'):
        nowlink = link.get('href')
        all_link_list.append(nowlink[6:])
for i in all_link_list:
    #print(i)
    if ':' not in i and not i.startswith('#') and 'hse' in i and 'pluginfile' not in i:
        all_link_list_new.append(i)
print(len(all_link_list_new))

