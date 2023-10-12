"""
本程序通过索引 ”:“ 以及 \‘ 或 \”来确定字典(dict)的key和value
假定key形如：’“key_name”‘ 或 “’key_name‘”
————Version：1.0
"""

'''
题目：
字典翻转输出
描述
读入一个字典类型的字符串，反转其中键值对输出。
即，读入字典key:value模式，输出value:key模式。
输入格式
用户输入的字典格式的字符串，如果输入不正确，提示：输入错误。
输出格式
给定字典d，按照print(d)方式输出
'''

def my_index(list1, value):
    num = list1.count(value)
    list2 = [list1.index(value)]

    for i in range(1, num):
        list2.append(list1.index(value, list2[i-1]+1))
    return list2

def dic_reverse(dic):
    dl = list(dic)  # dict list
    del dl[0]
    del dl[-1]
    yinhao_list = []
    yinhao1_list = []
    yinhao2_list = []
    if '\"' in dl:
        yinhao_list = yinhao1_list = my_index(dl, "\"")
    if '\'' in dl:
        yinhao2_list = my_index(dl, "\'")
        yinhao1_list.extend(yinhao2_list)
        yinhao_list = sorted(yinhao1_list)

    if (len(yinhao_list) == 0) and (":" in dl):
        print("输入错误")
        exit(0)

    if ":" not in dic:
        print("输入错误")
        exit(0)
    maohao_list = my_index(dl, ":")

    num = len(maohao_list)
    key_list = []
    value_list = []
    for j in range(num):
        key_list.append("".join(dl[yinhao_list[j * 2] + 1:maohao_list[j] - 1]))

    for j in range(num - 1):
        if dl[maohao_list[j]+1] != " ":
            if dl[yinhao_list[2*j+2]-1] != ' ':
                value_list.append("".join(dl[maohao_list[j] + 1:yinhao_list[2 * j + 2] - 1]))
            else:
                value_list.append("".join(dl[maohao_list[j] + 1:yinhao_list[2 * j + 2] - 2]))
        else:
            if dl[yinhao_list[2*j+2]-1] != ' ':
                value_list.append("".join(dl[maohao_list[j] + 2:yinhao_list[2 * j + 2] - 1]))
            else:
                value_list.append("".join(dl[maohao_list[j] + 2:yinhao_list[2 * j + 2] - 2]))

    if dl[maohao_list[num-1] + 1] != " ":
        value_list.append("".join(dl[maohao_list[num - 1] + 1:]))
    else:
        value_list.append("".join(dl[maohao_list[num-1] + 2:]))

    str1 = "{"
    str1 = str1 + value_list[0] + ":" + " " + "\'" + key_list[0] + "\'"  # v: 'k'
    for i in range(1, num - 1):
        str1 = str1 + "," + " " + value_list[i] + ":" + " " + "\'" + key_list[i] + "\'"

    if num > 1:
        str1 = str1 + ',' + ' ' + value_list[num - 1] + ":" + " " + "\'" + key_list[num - 1] + "\'"
    str1 = str1 + "}"
    print(str1)


if __name__ == "__main__":
    dic = input()
    if "{" not in dic or "}" not in dic:
        print("输入错误")
    elif '{' in dic and '}' in dic and \
            ':' not in dic and \
            "'" not in dic and \
            "\"" not in dic:
        print("{}")
    else:
        dic_reverse(dic)

# test {"a":1,"b":2,"c":3,"d":4}