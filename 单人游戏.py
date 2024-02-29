import 规则

def p1_robot():
    while True:
        p1 = input("请输入“石头”或“剪刀”或“布”或“退出”：\n")
        result = 规则.pve(p1)
        print(result)
        if result == "游戏结束":
            break
