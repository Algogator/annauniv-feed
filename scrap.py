import urllib.request as urllib2
from bs4 import BeautifulSoup
from functools import lru_cache
from db import setData
import hashlib
import datetime
# @lru_cache(maxsize=24)


def main_feed():
    LINK = "https://www.annauniv.edu/more.php"
    page = urllib2.urlopen(LINK)
    page1 = urllib2.urlopen(LINK)
    soup = BeautifulSoup(page, "html.parser")
    remote_data = page1.read()
    remote_hash = hashlib.md5(remote_data).hexdigest()

    data = {"md5": remote_hash, "date": datetime.datetime.now().isoformat(),
            "feed": []}
    html = soup.findAll('td', height="25")
    for i in html:
        # print(i.parent)
        x = i.find('a')
        if x:
            print(x)
            # redis_db.set('main_feed', main_feed())
            data["feed"].append({"link": x.get('href'),
                                 "text": x.getText()})
            # print("Link", x.get('href'))
            # print(x.getText())
    print(data)
    setData('main_feed', data)
