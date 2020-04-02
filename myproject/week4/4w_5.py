from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/reviews', methods=['POST'])
def write_reviews():
   title_receive = request.form['title_give']
   author_receive = request.form['author_give']
   review_receive = request.form['review_give']

   review = {
      'title' : title_receive,
      'author' : author_receive,
      'review' : review_receive
   }

   db.reviews.insert_one(review)

   return jsonify({'result' : 'success', 'msg' : '리뷰가 성공적으로 작성 되었지용용'})

@app.route('/reviews')
def find_reviews():

   reviews = list(db.reviews.find({},{'_id' : 0}))

   return jsonify({'result' : 'success', 'msg' : '리뷰를 조회 했지용용', 'reviews' : reviews})


# ## API 역할을 하는 부분
# @app.route('/test', methods=['POST'])
# def test_post():
#    title_receive = request.form['title_give']
#    print(title_receive)
#    return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

# @app.route('/test', methods=['GET'])
# def test_get():
#    title_receive = request.args.get('title_give')
#    print(title_receive)
#    return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)