import mysql.connector

# 创建数据库连接
db = mysql.connector.connect(
    host="localhost",  # MySQL服务器地址
    user="root",   # 用户名
    password="123456aA",  # 密码
    database="python"  # 数据库名称
)

# 创建游标对象，用于执行SQL查询
cursor = db.cursor()




#拿到游标
cursor.execute("select * from user")

result=cursor.fetchall()

for row in result:
    print(row)
