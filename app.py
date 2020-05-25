from flask import Flask
from bs4 import BeautifulSoup
import urllib.request

app = Flask(__name__)


@app.route('/<keyword>',methods=['GET'])
def fun(keyword):
  data = []
  url = "https://www.xn--thepratebay-fcb.com/proxy/go.php?url=s/?q="+keyword
  headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
  'Chrome/51.0.2704.63 Safari/537.36'}
  req = urllib.request.Request(url=url, headers=headers)
  res = urllib.request.urlopen(req)
  soup = BeautifulSoup(res.read().decode("utf-8"),features="html.parser")
  for tr in soup.find('table').find_all('tr'):
    if (tr.get('class') is None) :
      td = tr.find_all('td')
      if (len(td)>2):
        a = td[1].find_all('a')
        data.append({
          'title':a[0].get('title'),
          'href':a[1].get('href')
        })
  return {
    'message':'',
    'content':data
  }
