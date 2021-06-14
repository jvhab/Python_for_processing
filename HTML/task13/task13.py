import bs4
import urllib.request

def screeningURL(url):
    resp = urllib.request.urlopen(url)
    html = resp.read().decode('utf8')
    soup = bs4.BeautifulSoup(html, 'html.parser')
    set_url = set()
    list_url = []
    for link in soup.find_all('a'):
        if link.has_attr('href'):
            now = link.get('href')
            if not now.startswith('#') and 'hse' in now and 'pluginfile' not in now:
                list_url.append(now)
    for i in list_url:
        if ':' not in i[6:] and 'Wikipedia' not in i:
            set_url.add(i[6:])
    return set_url

mos = screeningURL('file:///C:/Users/%D0%9A%D0%BE%D1%81%D1%82%D1%8F/MyProject/HTML/task13/Moscow%20-%20Wikipedia.html')
newYork = screeningURL('file:///C:/Users/%D0%9A%D0%BE%D1%81%D1%82%D1%8F/MyProject/HTML/task13/New%20York%20City%20-%20Wikipedia.html')

all_url = (mos & newYork)
mysort = sorted(all_url)
for i in mysort:
    print(i)