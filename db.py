import redis
import json
redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)

def getData(key):
    data = redis_db.get(key)
    data = data.decode('utf-8')
    data = json.loads(data)
    return data

def setData(key, data):
    redis_db.set(key, json.dumps(data))
