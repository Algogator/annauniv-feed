from scrap import main_feed
from db import getData
import urllib.request as urllib2
import hashlib

def site_changed():
    data = getData('main_feed')
    remote_data = urllib2.urlopen('https://www.annauniv.edu/more.php').read()
    remote_hash = hashlib.md5(remote_data).hexdigest()
    if data["md5"] != remote_hash:
        print("Change in site!")
        main_feed()
        return True
    else:
        return False
