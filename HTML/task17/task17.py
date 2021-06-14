from bs4 import BeautifulSoup
import urllib.request

resp = urllib.request.urlopen('file:///C:/Users/%D0%9A%D0%BE%D1%81%D1%82%D1%8F/MyProject/HTML/task17/New%20York%20City%20-%20Wikipedia.html')
http = resp.read().decode('utf8')
soup = BeautifulSoup(http, 'html.parser')
a = soup.find_all('table', {'class': 'wikitable collapsible collapsed'})
file1 = open('aga.csv', 'w', encoding='utf8')
print(a[0].text, file=file1, sep=',', end='\n')
print(a[1].text, file=file1, sep=',', end='\n')
print(a[2].text, file=file1, sep=',')