from random import randint

clist = ["石头","剪刀","布","退出"]

def game(p1, p2):
    p1_ch = "p1输入" + p1
    p2_ch = "p2输入" + p2
    if (p1 not in clist) or (p2 not in clist):
        return "有玩家输入有误"
    elif p1 == "退出" or p2 == "退出":
        return "游戏结束"
    elif p1 == p2:
        return "{}\n{}\n平局".format(p1_ch,p2_ch)
    elif (p1 == "石头" and p2 == "剪刀") or (p1 == "剪刀" and p2 == "布") or (p1 == "布" and p2 == "石头"):
        return "{}\n{}\np1胜利".format(p1_ch,p2_ch)
    else:
        return "{}\n{}\np2胜利".format(p1_ch,p2_ch)

def pve(p1):
    p2 = clist[randint(0,2)]
    result = game(p1, p2)
    return result
    
def pvp(p1, p2):
    result = game(p1, p2)
    return result
