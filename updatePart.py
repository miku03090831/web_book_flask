import pymysql
def UpdateBook(conn,afterBook):
    try:
        cursor = conn.cursor()
        Id = afterBook['id']
        title = afterBook['title']
        author = afterBook['author']
        recommend = afterBook['recommend']
        price = afterBook['price']
        pic_refs = afterBook['pic_refs']
        sql = "update book set title = %s, author = %s, recommend = %s, price = %s, imageref = %s where id = %s"
        cursor.execute(sql,(title,author,recommend,price,pic_refs,Id))
        conn.commit()
        return "修改成功"
    except Exception as e:
        conn.rollback()
        return "修改失败"+"\n"+str(e)