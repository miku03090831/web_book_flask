from flask import Flask,request,abort,jsonify
import pymysql
import addPart
import selectPart
import deletePart
import updatePart
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
    f=request.files['addfile']
    fail = addPart.AddBatch(conn,f)
    if fail==-1:
        return jsonify(fail),401
    return jsonify(fail),200

@app.route("/api/SearchBook",methods=['POST'])
def SearchBook():
    search = request.json
    # print(search)
    result = selectPart.SelectBook(conn,search['keyword'],search['type'])
    if result=="bad":
        return jsonify(result),401
    print(len(result))
    return jsonify(result),200

@app.route("/api/DeleteBook",methods=['POST'])
def DeleteBook():
    delete = request.json
    print(delete)
    deletePart.DeleteBook(conn,delete['idArray'])
    return jsonify(delete),200

@app.route("/api/UpdateBook",methods=['POST'])
def UpdateBook():
    update = request.json
    print(update)
    result = updatePart.UpdateBook(conn,update)
    return jsonify(result),200

if __name__ == "__main__":
    app.run(debug=True)