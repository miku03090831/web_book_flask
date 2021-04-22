import pymysql
def DeleteBook(conn,idArray,lock):
    sql = "delete from book where id = %s"
    for num in idArray:
        try:
            cursor = conn.cursor()
            lock.acquire()
            cursor.execute(sql,str(num))
            lock.release()
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
