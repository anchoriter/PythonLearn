

# class Student(object):
#     pass


# s = Student()
#
# s.name = 'Michael'
#
# print(s.name)
#
#
# def set_age(self, age):
#     self.age = age
#
#
# from types import MethodType
#
# s.set_age = MethodType(set_age, s)
#
# s.set_age(24)
#
# print(s.age)
#
# s2 = Student()


# 动态绑定方法
# def set_score(self, score):
#     self.score = score
#
# Student.set_score = set_score
#
# s2.set_score(100)
#
# print(s2.score)



# 使用__slots__
#
# __slots__变量，来限制该class实例能添加的属性
# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：

# class Student(object):
#     __slots__ = ('name', 'age')
#
#
# s = Student()
#
# s.name = 'Tom'
# s.age = 12
# # s.score = 12
#
# class GraduateStudent(Student):
#     pass
#
# g = GraduateStudent()
#
#
# zhijianshare.com图片域名


# 使用@property
# class Student(object):
#
#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self,value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#

#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#
#
#         self._score = value
#
#     @property
#     def age(self):
#         return self._age
#
# s = Student()
#
# s.score = 60
#
# print(s.score)

# s.score = 300
#
# print(s.score)

# s.age = 20

# print(s.age)


# class Student(object):
#     def __init__(self,name):
#         self.name = name
#
#     def __str__(self):
#         return 'Student object (name: %s)' % self.name
#
#     __repr__ = __str__
#
# s = Student('Tom')
# print(s)
#
# s

#
# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1 # 初始化两个计数器a，b
#
#     def __iter__(self):
#         return self            # 实例本身就是迭代对象，故返回自己
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a+self.b
#
#         if self.a > 100000: # 退出循环条件
#             raise StopIteration()
#
#         return self.a
#
#     def __getitem__(self, n):
#         a, b = 1, 1
#
#         for x in range(n):
#             a, b = b, a+b
#
#         return a
#
# for n in Fib():
#     print(n)
#
#
# f = Fib()
# print(f[10])


# class Student(object):
#     def __init__(self):
#         self.name = 'Tom'
#
#     def __getattr__(self, attr):
#         if attr == 'score':
#             return 89
#
#         # if attr == 'age':
#         #     return lambda : 25
#
#         raise  AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
#
# s = Student()
# print(s.name)
# print(s.score)
# print(s.age)


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path,path))

    def __str__(self):
        return self._path

    __repr__ = __str__


cha = Chain()

print(cha.status.user.timeline.list)
















