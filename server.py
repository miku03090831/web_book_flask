from flask import Flask,request,abort,jsonify
import pymysql
import addPart
app=Flask(__name__)

conn = "123"

@app.route("/api/Login",methods=['POST'])
def login():
    username = request.json['userName']
    password = request.json['password']
    try:
        globals()['conn'].close  #如果之前已经有连接，先关闭连接
    except:
        pass
    # 登录mysql
    try:
        globals()['conn'] = pymysql.connect(
            host='localhost',
            port=3306,
            user=username,
            password=password,
            database='bookweb',
            charset='utf8'
        )   
        return 'login succcess',200
    except:
        return 'login failed',401
    

@app.route("/api/Addone",methods=['POST'])
def Addone():
    print(request.json)
    book = request.json
    # 调用添加的方法
    conn = globals()['conn']
    result = addPart.AddOne(conn,book['title'],book['recommend'],book['author'],book['price'],book['pic_refs'])
    if(result == 0):
        return "添加成功",200
    else:
        return result,200

@app.route("/api/AddFile",methods=['POST'])
def AddFile():
    print(request)
    return "服务器返回"

if __name__ == "__main__":
    app.run(debug=True)