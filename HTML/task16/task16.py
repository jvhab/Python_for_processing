from bs4 import BeautifulSoup
import urllib.request

resp = urllib.request.urlopen('file:///C:/Users/%D0%9A%D0%BE%D1%81%D1%82%D1%8F/MyProject/HTML/task16/task_7_6_3.html')
html = resp.read().decode('utf8')
soup = BeautifulSoup(html, 'html.parser')
a = [int(i.text) for i in soup.find_all('td')]
result = sum(a)
print(result)
