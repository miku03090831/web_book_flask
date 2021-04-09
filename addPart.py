import pymysql

def AddOne(conn,title,recommend,author,price,imageref):
    cursor = conn.cursor()
    try:
        sql = "select * from book where title=%s"
        cursor.execute(sql,title)
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
