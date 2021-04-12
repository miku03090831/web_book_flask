import pymysql
def DeleteBook(conn,idArray):
    sql = "delete from book where id = %s"
    for id in idArray:
        try:
            cursor = conn.cursor()
            cursor.execute(sql,id)
            conn.commit()
        except:
            conn.rollback()
