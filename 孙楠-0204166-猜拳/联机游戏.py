import socket
import 规则
import 获取公网ip

def p1_socket():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 获取公网ip.get_ip()
    #host = socket.gethostbyname(socket.gethostname())
    print("p2输入{}即可建立连接".format(host))
    server_socket.bind(('127.0.0.1', 51778))
    server_socket.listen(1)
    client_socket,addr = server_socket.accept()
    while True:
        p1 = input("请输入“石头”或“剪刀”或“布”或“退出”：\n")
        p2 = client_socket.recv(32).decode('utf-8')
        result = 规则.pvp(p1, p2)
        print(result)
        client_socket.send(result.encode('utf-8'))
        if result == "游戏结束":
            client_socket.close()
            break

def p2_socket():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input("请输入p1玩家ip")
    client_socket.connect(('127.0.0.1', 51778))
    while True:
        p2 = input("请输入“石头”或“剪刀”或“布”或“退出”：\n")
        client_socket.send(p2.encode('utf-8'))
        result = client_socket.recv(128).decode('utf-8')
        print(result)
        if result == "游戏结束":
            client_socket.close()
            break
