'''
V2.0 
warning: 本算法使用了eval（）函数，请慎用
'''

def dict_reverse():
    try:
        dic = eval(input())
    except SyntaxError:
        print("输入错误")
    else:
        if str(type(dic)) != str(type({})):
            print("输入错误")
        else:
            key = list(dic.keys())
            value = list(dic.values())
            dic2 = dict(zip(value, key))
            return dic2


        # dic2 = {i:k for i,k in zip(key,value)}
