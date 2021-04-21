import pymysql
import csv
import json

def AddOne(conn,title,recommend,author,price,imageref):
    try:
        cursor = conn.cursor()
        sql = "select * from book where title=%s and author=%s"
        cursor.execute(sql,(title,author))
        exist = cursor.fetchone()
        if exist is None:
            sql = "insert into book values(0,%s,%s,%s,%s,%s)"
            price = float(price)
            cursor.execute(sql,(title,recommend,author,price,imageref))
            conn.commit()
        else:
            raise Exception("添加失败，已存在同名书籍")
        return 0
    except Exception as e:
        conn.rollback()
        errmsg = "%s" % e
        print(errmsg)
        return errmsg

def AddBatch(conn,file):
    try:
        items = file.read().decode('utf-8').split("}")[:-1]
        failList = []
        for item in items:
            item = item+"}"
            item = json.loads(item)
            title = item['title']
            recommend = item['recommend']
            author = item['author']
            price = item['price']
            imageref = item['iamge']
            print(title+" "+recommend+" "+author+" "+price+" "+imageref)
            add = AddOne(conn,title,recommend,author,price,imageref)
            if add!=0:
                failList.append({'title':title,'reason':add})
        return failList
    except Exception as e:
        errmsg = "%s" % e
        print(errmsg)
        return -1
        
    
    
