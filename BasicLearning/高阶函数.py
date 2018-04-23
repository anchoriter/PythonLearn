

def add(x,y,f):
    return (f(x)+f(y))


print(add(-5,6,abs))

def f(x):
    return x * x

r = map(f,[1,2,3,4,5,6])
arr = list(r)
print(arr)

m = list(map(str,arr))
print(m)

from functools import reduce

def add(x,y):
    return x+y

s = reduce(add,[1,2,3])
print(s)

def fn(x,y):
    return x*10+y

s1 = reduce(fn,[1,2,3])
print(s1)

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

s2 = reduce(fn,map(char2num,'12579'))
print(s2)


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

s3 = str2int('12345679')
print(s3)


def char2num(s):
    return DIGITS[s]
def str2int(s):
    return reduce()




def is_odd(n):
    return n % 2 == 1

l = list(filter(is_odd,[1,2,3,4,5,6]))
print('filter==',l)

def not_empty(s):
    return s and s.strip()

l1 = list(filter(not_empty,['a','',None,' ']))
print('filter==',l1)

# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，
# filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。