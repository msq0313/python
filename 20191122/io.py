import time

from exercise_04 import makesentence

times = int(input("请输入要生成文本的行数："))


def deco1(func):  # 定义函数deco1
    def inner1(*args, **kwargs):  # 定义函数inner1
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()
        print("用时：", t2 - t1, "秒\n")

    return inner1  # 返回函数inner1的引用


@deco1
def open_close_file(filename):
    print("打开关闭函数启动")
    infile = open(filename)
    infile.close()


@deco1
def write_file(filename):
    print("写入函数启动")
    infile = open(filename, "w")
    for i in range(times):
        string = " ".join(makesentence.sentence()) + '\n'
        infile.write(string)
    infile.close()


@deco1
def pickA_file(filename):
    print("提取cat方式A启动")
    infile = open(filename)
    l1 = list(map(str, infile.read().split()))
    l2 = []
    for s in l1:
        if s == 'cat':
            l2.append(s)
    infile.close()
    print("出现次数：", len(l2))


@deco1
def pickB_file(filename):
    print("提取cat方式B启动")
    # 定义需要的全局变量
    file = None
    l2 = []  # 保存cat字符串

    # 定义打开文件的函数
    def open_file(filename):
        nonlocal file
        file = open(filename)

    # 定义读取一行数据的函数
    def next_cat():
        nonlocal l2, file  # 缓冲式处理，使用全局变量
        line = 1
        while line:
            line = file.readline()  # 读一行数据
            l1 = line.split()  # 切分单词
            for s in l1:
                if s == 'cat':
                    l2.append(s)
        print("出现次数：", len(l2))
        file.close()

    open_file(filename)
    next_cat()


@deco1
def pickC_file(filename):
    print("提取cat方式C启动")

    def outer(filename):
        # 定义局部函数
        l2 = []
        file = open(filename)

        # 内部函数
        def inner():
            nonlocal l2, file
            line = 1
            while line:
                line = file.readline()
                l1 = line.split()
                for s in l1:
                    if s == 'cat':
                        l2.append(s)
            print("cat出现次数：", len(l2))

        return inner  # 返回局部定义的函数对象

    pick = outer(filename)
    pick()


def main():
    open_close_file("data.txt")
    write_file("data.txt")
    pickA_file("data.txt")
    pickB_file("data.txt")
    pickC_file("data.txt")


# 入口函数
if __name__ == '__main__':
    main()
