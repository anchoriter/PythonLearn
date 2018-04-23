

# f = open('/Users/Anchoriter/Desktop/ZJLeftLifepr.json', 'r')
# print(f.read())



# with open('/Users/Anchoriter/Desktop/ZJLeftLifepr.json', 'r') as f:
#     print(f.read())



# with open('/Users/Anchoriter/Desktop/ZJLeftLifepr.json', 'r') as f:
#     for line in f.readlines():
#         print(line.strip())



# with open('/Users/Anchoriter/Desktop/ZJLeftLifepr.json', 'rb') as f:
#     for line in f.readlines():
#         print(line.strip())



# with open('/Users/Anchoriter/Desktop/ZJLeftLifepr.json', 'r', errors='ignore') as f:
#         print(f.read())



# from io import StringIO

# f = StringIO()
#
# print(f.write('hello'))
#
# print(f.write(' '))
#
# print(f.write('world!'))
#
# print(f.getvalue())


# from io import StringIO
# f = StringIO('Hello!\nHi!\nGoodbye!')
#
# while True:
#     s = f.readline()
#     if s == '':
#         break
#
#     print(s.strip())




# from io import BytesIO
#
# f = BytesIO()
#
# f.write('中文'.encode('utf-8'))
#
# print(f.getvalue())



# import os
#
# print(os.environ.get('PATH'))

# print(os.environ.get('x', 'default'))

# 查看当前目录的绝对路径:
# print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# print(os.path.join('/Users/Anchoriter/Desktop/Anchoriter/Python', 'testdir'))
# 然后创建一个目录:
# print(os.mkdir('/Users/Anchoriter/Desktop/Anchoriter/Python/testdir'))
# 删掉一个目录:
# print(os.rmdir('/Users/Anchoriter/Desktop/Anchoriter/Python/testdir'))



# print(os.mkdir('/Users/Anchoriter/Desktop/Anchoriter/Python/testdir/file.txt'))
# 把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
# print(os.path.split('/Users/Anchoriter/Desktop/Anchoriter/Python/testdir/file.txt'))
# 直接让你得到文件扩展名
# print(os.path.splitext('/Users/Anchoriter/Desktop/Anchoriter/Python/testdir/file.txt'))

# print(os.mkdir('/Users/Anchoriter/Desktop/Anchoriter/Python/testdir/test.txt'))
# os.rename('/Users/Anchoriter/Desktop/Anchoriter/Python/testdir/test.txt', '/Users/Anchoriter/Desktop/Anchoriter/Python/testdir/test.py')

# os.remove('/Users/Anchoriter/Desktop/Anchoriter/Python/testdir/test.py')


# print([x for x in os.listdir('.') if os.path.isdir(x)])
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])




# import os
#
# print('Progress (%s) start...' % os.getpid())
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
#
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


import time, threading

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
# 启动线程
t.start()
# 等待子进程结束后再继续往下运行，通常用于进程间的同步。
t.join()
print('thread %s ended.' % threading.current_thread().name)









