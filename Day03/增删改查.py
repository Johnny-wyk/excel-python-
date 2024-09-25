import mysql.connector
import pymysql
# 创建数据库连接
db = pymysql.connect(
    host="localhost",  # MySQL服务器地址
    user="root",   # 用户名
    password="123456aA",  # 密码
    database="python"  # 数据库名称
)

# 创建游标对象，用于执行SQL查询
#cursor = db.cursor()
#字典形式
cursor=db.cursor(pymysql.cursors.DictCursor)

###增删改
# sql="insert into user(name,sex,age) values(%s,%s,%s)"
# rows=cursor.execute(sql,("sb","男",23))
# print(rows)

db.commit()

#查询
cursor.execute("select * from user")

cursor.scroll(1,'absolute')
cursor.scroll(1,mode='relative')

result=cursor.fetchall()

for row in result:
    print(row)


#关闭
cursor.close()
db.close()