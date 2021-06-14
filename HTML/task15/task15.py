import bs4
import urllib.request

resp = urllib.request.urlopen('file:///C:/Users/%D0%9A%D0%BE%D1%81%D1%82%D1%8F/MyProject/HTML/task15/task_7_6_2.html')
html = resp.read().decode('utf8')
soup = bs4.BeautifulSoup(html, 'html.parser')

all_num = [int(i.text) for i in soup.find_all('td')]
result = sum(all_num)
print(result)