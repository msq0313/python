import time
import makesentence
''' 写入200M数据，统计cat出现次数并将所有cat写入列表
    探究一次读入和分行读入的速度差异
    由于统计算法对程序影响很大，本题统一使用for循环统计'''


# 使用一个装饰器即可完成功能，此处为直观，使用三个
# 装饰器
def deco1(func):
    def inner1(*args, **kwargs):
        print('一次读入方法实现开始')
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        time1 = end_time - start_time
        print("函数运行时间:", time1)
        print('一次读入方法实现结束')
    return inner1


def deco2(func):
    def inner2(*args, **kwargs):
        print('打开文件方法实现开始')
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        time2 = end_time - start_time
        print("函数运行时间:", time2)
        print('打开文件方法技术实现结束')
    return inner2


def deco3(func):
    def inner3(*args, **kwargs):
        print('逐行读入方法实现开始')
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        time2 = end_time - start_time
        print("函数运行时间:", time2)
        print('逐行读入方法技术实现结束')
    return inner3


# 打开关闭文件
def open_close():
    f = open('/Users/zhengbo/PycharmProjects/python_homework/IO_practice/data.txt')
    f.close()


# 写入数据
def write_in():
    f = open('/Users/zhengbo/PycharmProjects/python_homework/IO_practice/data.txt', 'w')
    # 10000000 次大约为 200M
    for i in range(1000000):
        strr1 = " ".join(makesentence.sentence())
        strr2 = strr1 + '.' + '\n'
        f.write(strr2)


# 第一种方法，整体读入
@deco1
def find_cat1(fname):
    file1 = open(fname)
    # map统计，速度较慢
    # count = sum(map(lambda x: x == 'cat', file1.read().split()))
    # 用filter对应，在转换为list统计个数，速度稍快，但没有for快
    # count = list(filter(lambda x: x == 'cat', file1.read().split()))
    # map映射，速度很慢
    # s = list(map(str, file1.read().split()))
    # 读取后按单词切分
    s = file1.read().split()
    # 直接读取方法，速度最快
    # s = file1.read()
    # count = s.count('cat')
    # cat_list1 = []
    # for i in range(count):
    #     cat_list1.append('cat')
    count = 0   # 计数
    cat_list1 = []  # 保存所有的cat
    for i in s:
        if i == 'cat':
            count += 1
            cat_list1.append(i)
    # print(s)
    # print(cat_list1)
    print('cat number: ', count)
    file1.close()


# 第二种方法,逐行读入,使用两个函数实现
# 定义全局变量
file2 = None
nlist = []


# 打开函数
@deco2
def open_file(fname):
    global file2
    file2 = open(fname)


# 查找函数
@deco3
def find_cat2():
    global nlist
    count = 0
    cat_list = []
    line = 1
    while line:
        line = file2.readline()
        nlist = line.split()
        for j in nlist:
            if j == 'cat':
                count += 1
                cat_list.append(j)
    print('cat number: ', count)
    file2.close()
    # print(cat_list)


# 第三种方法，闭包实现
# 闭包
def outer_f(fname):
    cat_list = []
    file3 = open(fname)
    count = 0

    # 内部函数
    def inner_f():
        nonlocal cat_list, count
        line = 1
        while line:
            line = file3.readline()
            nlist2 = line.split()
            for j in nlist2:
                if j == 'cat':
                    cat_list.append(j)
                    count += 1
        # for循环写法，根据文件选择遍历次数，不建议使用
        # for i in range(1000000):
        #     # 逐行读取
        #     line = file3.readline()
        #     if not line:
        #         file3.close()
        #         return None
        #     # 每行内容
        #     nlist2 = line.split()
        #     # 逐行统计
        #     for j in nlist2:
        #         if j == 'cat':
        #             cat_list.append(j)
        #             count += 1
        #     print(nlist2)
        # print(cat_list)
        print('cat number: ', count)
        return nlist2

    return inner_f


@deco2
def find_cat3():
    f_c3 = outer_f("/Users/zhengbo/PycharmProjects/python_homework/IO_practice/data.txt")
    f_c3()


if __name__ == '__main__':
    # 写入数据
    write_in()
    # 一次读入方法
    # find_cat1('/Users/zhengbo/PycharmProjects/python_homework/IO_practice/data.txt')
    # 逐行读入方法
    # open_file('/Users/zhengbo/PycharmProjects/python_homework/IO_practice/data.txt')
    # find_cat2()
    # 闭包方法
    # find_cat3()




