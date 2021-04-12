import pymysql
import json
def SelectBook(conn,keyword,searchType):
    try:
        cursor = conn.cursor()
        if(searchType==3):
            sql = "select id,title,author,recommend,price,imageref from book where id=%s"
        elif(searchType==4):
            sql = "select id,title,author,recommend,price,imageref from book where title=%s"
        elif(searchType==5):
            sql = "select id,title,author,recommend,price,imageref from book where author=%s"
        cursor.execute(sql,keyword)
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
        return jsonResult
    except:
        conn.rollback()