import bs4
import urllib.request

def scriningURL(url):
    response = urllib.request.urlopen(url)
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
    return len(all_link_list_new)
print(scriningURL('file:///C:/Users/%D0%9A%D0%BE%D1%81%D1%82%D1%8F/MyProject/HTML/task11/Moscow%20-%20Wikipedia.html'))
print(scriningURL('file:///C:/Users/%D0%9A%D0%BE%D1%81%D1%82%D1%8F/MyProject/HTML/task11/New%20York%20City%20-%20Wikipedia.html'))