import pymysql
import 获取公网ip
from socket import gethostbyname,gethostname

def connect_database():
    connection = pymysql.connect(
        host="localhost",
        port = 3306,
        user="root",
        password="123456",
        database = "sun"
        )
    if (connection):
        return connection

def register(username, md5_password):
    connection = connect_database()
    if (connection):
        sql1 = "select 1 from user where username = '{}' limit 1;".format(username)
        sql2 = "insert into user(username, password, ip) values ('{}','{}','');".format(username, md5_password)
        with connection.cursor() as cur:
            cur.execute(sql1)
            cur.connection.commit()
            result = cur.fetchall()
            if result == ():
                cur.execute(sql2)
                cur.connection.commit()
                print("注册成功")
                return True
            elif result[0][0] == 1:
                print("用户名已存在")
                return False

def login(username, md5_password):
    connection = connect_database()
    if (connection):
        sql1 = "select password,ip from user where username = '{}';".format(username)
        sql2 = "update user set ip = '{}' where username = '{}';".format(获取公网ip.get_ip(), username)
        #sql2 = "update user set ip = '{}' where username = '{}';".format(gethostbyname(gethostname()), username)
        with connection.cursor() as cur:
            cur.execute(sql1)
            cur.connection.commit()
            result = cur.fetchall()
            if result != () and result[0][1] != '':
                print("账号已登录")
                return 0
            elif result != () and md5_password == result[0][0]:
                cur.execute(sql2)
                cur.connection.commit()
                print("登陆成功")
                return True
            else:
                print("用户名或密码错误")
                return -1

def logout(username):
    connection = connect_database()
    if (connection):
        sql1 = "update user set ip = '' where username = '{}';".format(username)
        with connection.cursor() as cur:
            cur.execute(sql1)
            cur.connection.commit()


