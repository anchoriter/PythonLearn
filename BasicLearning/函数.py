n = abs(-199.12)
print(n)

a = abs

print(a(-100))

n1 = 255
n2 = 1000
h1 = hex(255)
h2 = hex(1000)
print(h1)
print(h2)

# 定义函数
def my_abs(x):
    if x > 10 :
        return x
    else:
        return -x

print(my_abs(-100))

def nop():
    pass

nop()

# if age >= 18:
#     pass

# print(abs('abc'))
# print(my_abs('abc'))



def m_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# print(m_abs('111'))



import  math

def move (x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.cos(angle)

    return nx, ny

x, y = move(100,100,60,math.pi/6)
print(x,y)

r = move(100,100,60,math.pi/6)
print(r)

# ax2 + bx + c = 0
# def quadratic(a, b, c):
#     if not isinstance(a,(int,float)) or not isinstance(b,(int,float)) or not isinstance(c,(int,float)):
#         raise TypeError('bad operand type')
#     d = (bb-(4ac))
#     if d < 0:
#         return ('无解')
#     elif d == 0:
#         return ('方程式有一个解：%s' %(-b/(2a)))
#     else:
#         x1 = (-b + math.sqrt(d)) / (2a)
#         x2 = (-b - math.sqrt(d)) / (2a)
#
#         return ('方程有两个解:%.2f %.2f' % (x1, x2))

# 函数的参数


def power(x,n=2):
    s= 1
    while n > 0:
        n = n - 1
        s = s * x

    return s

print(power(2,4))

# 递归  汉诺塔
def move(n,a,b,c):
    if n == 1:
        print('move',a,'-->',c)

    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)


move(4,'A','B','C')

# 切片
def trim(s):
    headStr = s[:1]
    footStr = s[-1:]
    if headStr == " " or footStr == " ":
        print('测试失败')
    else:
        print('测试成功')

trim('hello')

# 迭代
d = {'a': 1, 'b': 2, 'c': 3}

for k,v in d.items():
    print(k,v)

for ch in 'ABCD':
    print(ch)

# 判断一个对象是可迭代对象
from collections import Iterable

print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance((1,2,3),Iterable))
print(isinstance(123,Iterable))  # 整数不可迭代
print(isinstance('   ',Iterable))

for i,value in enumerate(['A','B','C']):
    print(i,value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x,y)


def findMinAndMax (L):
    max = L[0]
    min = L[0]
    for n in L:
        if min > n:
            min = n
        if max < n:
            max = n

    return (min, max)


L = [4,5,10,9,7,12,21]
a,b = findMinAndMax(L)
print('最小值 =',a,'最大值 =', b)

# 列表生成式

arr = list(range(1,3))
print(arr)

# [1x1, 2x2, 3x3, ..., 10x10]
arr1 = [x*x for x in range(1,5)]
print(arr1)

# 筛选出仅偶数的平方
arr2 = [x*x for x in range(1,5) if x%2 == 0]
print(arr2)

# 两层循环
arr3 = [m+n for m in 'abc' for n in 'xyz']
print(arr3)

# 列出当前目录下的所有文件和目录名
import os # 导入os模块

arr4 = [d for d in os.listdir('.')]
print(arr4)

# 列表生成式也可以使用两个变量来生成list
d = {'x':'A','y':'B','z':'C'}
for k,v in d.items():
    print(k,'=',v)


strr = [k+'='+v for k,v in d.items()]
print(strr)


L = ['Hello', 'World', 'IBM', 'Apple']
H = ['hello', 'world', 'ibm', 'apple']

# 把一个list中所有的字符串变成小写：
str1 = [s.lower() for s in L]
print(str1)
# 把一个list中所有的字符串变成大写：
str2 = [s.lstrip() for s in L]
print(str2)


# 练习 : 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = []
from collections import Iterable
for l in L1:
    if isinstance(l,str):
        L2.append(l)


L2 = [s.lower() for s in L2]
print(L1)
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')




# 迭代器
# 可以直接作用于for循环的对象统称为可迭代对象：Iterable。
# 是否是Iterable对象：

from collections import Iterable
print('Iterable')

isin = isinstance([],Iterable)
print(isin)

isin1 = isinstance({},Iterable)
print(isin1)

isin2 = isinstance('abc',Iterable)
print(isin2)

isin3 = isinstance((x for x in  range(10)),Iterable)
print(isin3)

isin4 = isinstance(100,Iterable)
print(isin4)

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

from collections import Iterator
print('Iterator')

isin5 = isinstance((x for x in range(10)),Iterator)
print(isin5)

isin6 = isinstance([],Iterator)
print(isin6)

isin7 = isinstance({},Iterator)
print(isin7)

isin8 = isinstance('abc',Iterator)
print(isin8)

isin9 = isinstance(100,Iterator)
print(isin9)


# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。

# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：


isin10 = isinstance(iter([]),Iterator)
print(isin10)

isin11 = isinstance(iter({}),Iterator)
print(isin11)

isin12 = isinstance(iter('abc'),Iterator)
print(isin12)


# 凡是可作用于for循环的对象都是Iterable类型；
#
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

















