



# class Student(object):
#     pass
#
# bart = Student()
#
# print(bart)
#
# print(Student)
#
# bart.name = 'Bart Simpson'
# print('名字是：' + bart.name)




# class Student(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
# bart1 = Student('Tom', 89)
#
# print('名字：'+bart1.name)
# print(bart1.score)
#
# def print_score(std):
#     print('%s: %s' % (std.name,std.score))
#
#
# print_score(bart1)




# class Student(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print('%s: %s' % (self.name, self.score))
#
# bart1 = Student('Tom', 89)
#
# bart1.print_score()




# class Student(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print('%s: %s' % (self.name, self.score))
#
#
#     def get_grade(self):
#         if self.score >= 90:
#             return 'A'
#
#         elif self.score >= 60:
#             return 'B'
#
#         else:
#             return 'C'
#
#
# bart1 = Student('Tom', 92)
# bart2 = Student('Lisa', 69)
# bart3 = Student('Bart', 30)
#
# print(bart1.name, bart1.get_grade())
# print(bart2.name, bart2.get_grade())
# print(bart3.name, bart3.get_grade())
#
#
# bart1.age = 10
#
# print(bart1.age)
#
# print(bart2.age)


# 访问限制

# class Student(object):
#
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#
#     def print_score(self):
#         print('%s: %s' % (self.__name, self.__score))
#
#     def get_name(self):
#         return self.__name
#
#     def get_score(self):
#         return self.__score
#
#     def set_name(self, name):
#         self.__name = name
#
#     def set_score(self, score):
#         self.__score = score
#
#
# bart = Student('Bart Simpson', 49)
#
# print(bart.get_name())
#
# print(bart.get_score())
#
# bart.set_score(88)
# print(bart.get_score())



# 继承和多态

# class Animal(object):
#     def run(self):
#         print('Animal is running...')
#
#
# class Dog(Animal):
#     def run(self):
#         print('Dog is running...')
#
#     def eat(self):
#         print('Eating meat...')
#
# class Cat(Animal):
#     def run(self):
#         print('Cat is running...')

# dog = Dog()
# dog.run()
# dog.eat()
#
# cat = Cat()
# cat.run()
#
# print(isinstance(dog,Dog))
# print(isinstance(dog,Animal))



# 获取对象信息

# a = Animal()
# print(type(a))
#
# print(type('123')==type('sadsad'))
#
# import types
#
# def fn():
#     pass
#
# print(type(fn)==types.FunctionType)
#
#
# print(isinstance(a,Animal))
#
# print(isinstance([1,2,3],(list,tuple)))
#
# print(dir(a))



# 使用dir

class MyObject(object):

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()

print(hasattr(obj, 'x')) # 有属性'x'吗？

print(obj.x)

print(hasattr(obj, 'y'))

setattr(obj, 'y', 90)

print(hasattr(obj, 'y'))

print(getattr(obj, 'y'))

print(obj.y)

print(getattr(obj,'z', 404))


print('获得对象的方法')


print(hasattr(obj, 'power'))

print(getattr(obj, 'power'))

fn = getattr(obj, 'power')

print(fn)

print(fn())








