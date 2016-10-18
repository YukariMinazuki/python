# -*- coding: UTF-8 -*-

# 输入和输出
name = input("\n请输入你的名字")  # "\n\n"在结果输出前会输出两个新的空行
print("hello", name)
print('hello,world')
print('hello', '你好', 'bye')
print('1024*768=', 1024 * 768)

# 变量赋值
counter = 100  # 赋值整型变量 不需要类型声明
a1 = b1 = c1 = 1;
a2, b2, c2 = 1, 2, 'sakana'  # 多个对象赋值
print(c2[2:])  # 索引(列表通用)
print(c2 + "baka")  # 连接输出(列表通用)

list = ['abcd', 123, 'edg']  # 创建一个列表
print(list)

tuple = ('abcd', 123, 'edg')  # 创建一个元组(状态不可以更新)

dict = {'name': 'yukari', 'age': 18}  # 创建一个字典，字典由key和它对应的值value组成
print(dict.keys())  # 输出所有键
print(dict.values())  # 输出所有值

print('\\\t\\')
print(r'\\\t\\')  # 内容不需要转义

print("Hello %s,I %s you" % ("Yukari", "love"))
print("My name is %s and weight is %d kg!" % ('Zara', 21))
