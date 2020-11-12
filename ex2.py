import DB_UTIL as db
con = db.db_connect()
a = db.check_capacity(con, 1)
print(a)
print(type(a))
con.close()