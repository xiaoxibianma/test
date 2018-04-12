import sys, bs4, webbrowser, requests

Topic = ' '.join(sys.argv[1:])
files = requests.get('http://www.baidu.com/s?wd=' + Topic)
files.raise_for_status()
soup = bs4.BeautifulSoup(files.text, "html.parser")
link = soup.select('.t a')

#print(link[1].get('href'))
number = min(6, len(link))
for i in range(3):
    webbrowser.open(link[i].get('href'))
