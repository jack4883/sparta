from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##

cinema = db.movies.find_one({'title': '어벤져스: 엔드게임'})
star = cinema['star']

db.movies.update_many({'star': star}, {'$set': {'star': 0}})
