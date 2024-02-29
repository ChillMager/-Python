from hashlib import md5
import sys
import 规则
import 单人游戏
import 账号操作
import 联机游戏

login_username = ""
while True:
    mod = input("选择游戏类型编号：\n1.单人游戏\n2.联机游戏\n3.退出\n")
    if mod == "1":
        单人游戏.p1_robot()
    if mod == "2":
        while True:
            c = input("联机游戏需要登录，请选择账号操作编号：\n1.注册\n2.登录\n3.退出并注销\n")
            if c == "1":
                username = input("请输入用户名")
                password = input("请输入密码")
                md5_password = md5(password.encode('utf-8')).hexdigest()
                账号操作.register(username, md5_password)
            elif c == "2":
                username = input("请输入用户名")
                password = input("请输入密码")
                md5_password = md5(password.encode('utf-8')).hexdigest()
                result = 账号操作.login(username, md5_password)
                if result == True:
                    login_username = username
                    while True:
                        pn = input("选择玩家编号：\n1.P1\n2.P2\n退出\n")
                        if pn == "1":
                            联机游戏.p1_socket()
                        elif pn == "2":
                            联机游戏.p2_socket()
                        elif pn == "3":
                            break
                        else:
                            print("输入有误")
            elif c == "3":
                账号操作.logout(login_username)
                break
            else:
                print('输入有误')
    if mod == "3":
        break
