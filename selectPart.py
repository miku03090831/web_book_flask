import pymysql
import json
def SelectBook(conn,keyword,searchType,lock):
    if type(conn)==type(""):
        return "bad"
    try:
        cursor = conn.cursor()
        if searchType==7:
            sql = "select id,title,author,recommend,price,imageref from book"
            lock.acquire()
            cursor.execute(sql)
            lock.release()
        else:
            if(searchType==3):
                sql = "select id,title,author,recommend,price,imageref from book where id=%s"
            elif(searchType==4):
                sql = "select id,title,author,recommend,price,imageref from book where title=%s"
            elif(searchType==5):
                sql = "select id,title,author,recommend,price,imageref from book where author=%s"
            lock.acquire()
            cursor.execute(sql,keyword)
            lock.release()
        conn.commit()
        result = cursor.fetchall()
        jsonResult=[]
        for item in result:
            book={}
            book['id']=item[0]
            book['title']=item[1]
            book['author']=item[2]
            book['recommend']=item[3]
            book['price']=float(item[4])
            book['pic_refs']=item[5]
            jsonResult.append(book)
        if len(jsonResult)==0:
            return "bad"
        return jsonResult
    except:
        conn.rollback()