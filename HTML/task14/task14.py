import bs4
import urllib.request
mysum = 0
resp = urllib.request.urlopen('file:///C:/Users/%D0%9A%D0%BE%D1%81%D1%82%D1%8F/MyProject/HTML/task14/task_7_6_1.html')
http = resp.read().decode('utf8')
soup = bs4.BeautifulSoup(http, 'html.parser')
for row in soup.find_all('td'):
    for i in row:
        ints = int(i)
        mysum += ints
print(mysum)