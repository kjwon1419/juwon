from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/orders', methods=['POST'])
def write_order():
   valueid = request.form['valueid']
   valuead = request.form['valuead']
   valuephone = request.form['valuephone']
   valuecount = request.form['valuecount']

   doc = {
        'name' : valueid,
        'count' : valuecount,
        'address' : valuead,
        'phone' : valuephone
   }
   db.orders.insert_one(doc)
	# 3. 성공 여부 & 성공 메시지 반환하기
   return jsonify({'result': 'success', 'msg': '주문이 성공적으로 접수되었습니다.'})


@app.route('/orders', methods=['GET'])
def read_reviews():
    orders = list(db.orders.find({},{'_id':False}))
    return jsonify({'result':'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)