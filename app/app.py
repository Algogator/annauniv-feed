from flask import Flask
from db import getData
import dateutil.parser
from monitor import site_changed
from scrap import main_feed
from flask import request
from werkzeug.contrib.atom import AtomFeed
app = Flask(__name__)


@app.route('/mainfeed')
def recent_feed():
    feed = AtomFeed('Main Feed',
                    feed_url=request.url, url=request.url_root)
    if site_changed():
        main_feed()
    data = getData('main_feed')
    for d in data['feed']:
        feed.add(d['text'],
                 url=d['link'],
                 updated=dateutil.parser.parse(data['date']))
    return feed.get_response()


if __name__ == "__main__":
    app.run()
