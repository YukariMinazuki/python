#  请打印出以下变量的值

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(n, f, s1, s2, s3, s4)
print()

#  计算小明成绩提升的百分点，并用字符串格式化显示

s1 = 72
s2 = 85
r = 85/100-72/100
print("小明成绩提升了%s百分点" % r)
print()

#  请用索引取出下面list的指定元素

L = [['Apple', 'Google', 'Microsoft'], ['Java', 'Python', 'Ruby', 'PHP'], ['Adam', 'Bart', 'Lisa']]

print("打印Apple:", L[0][0])
print("打印Python:", L[1][1])
print("打印Lisa:", L[2][2])
print()

#  打印小明的肥胖结果

height = 1.75
weight = 80.5
bmi = round(height/weight*weight)
if bmi < 18.5:
    print("小明的体重过轻")
elif 18.5 < bmi < 25:
    print("小明的体重正常")
elif 25 < bmi < 28:
    print("小明的体重过重")
elif 28 < bmi < 31:
    print("胖子小明")
elif bmi > 32:
    print("死胖子小明")
else:
    print("啊噢，计算有误哦")
print()

#  请利用循环依次对list中的每个名字打印出Hello, xxx!：

l = ['tom', 'bob', 'sakana']
for name in l:
    print('hello,', l)
print()

#  请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串

n1 = 255
n2 = 1000
print(hex(n1), hex(n2))
print()

#  请定义一个函数quadratic(a, b, c)，接收3个参数，返回相乘结果

a = int(input("请输入a的值"))
b = int(input("请输入b的值"))
c = int(input("请输入c的值"))


def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError('啊哦，输入类型不对哦')
    d = a*b*c
    return d
print(quadratic(a, b, c))
print()

#  请修改列表生成式，通过添加if语句保证列表生成式能正确地执行
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
print()

#  利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。


def normalize(name):
    return name.capitalize()  # 自动把首字母大写其余小写

B1 = ["adam", "LISA", "barT"]
B2 = list(map(normalize, B1))
print(B2)
print()

#  请利用filter()滤掉非回数：


def is_palindrome(o):
    return int(str(o)[::-1]) == o
output = filter(is_palindrome, range(1, 100))
print(list(output))
print()

#  请用sorted()对上述列表分别按名字，成绩排序：

Student = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(Stu):
    return Stu[0].lower()


def by_score(t):
    return t[1]
Student2 = sorted(Student, key=by_name)  # key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。
Student3 = sorted(Student, key=by_score, reverse=True)
print(Student2)
print(Student3)
print()