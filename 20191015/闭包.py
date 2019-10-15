def outer(x):  # 定义函数outer
    y = 10  # 定义局部变量y并赋为10

    def inner(z):  # 在outer函数中定义#嵌套函数inner
        nonlocal x, y  # nonlocal声明
        return x + y + z  # 返回x+y+z的结果

    return inner  # 返回嵌套函数
f = outer(5)  # 将返回的inner函数赋给f
g = outer(50)  # 将返回的inner函数赋给g
print('f(20)的值为：', f(20))
print('g(20)的值为：', g(20))
print('f(30)的值为：', f(30))
print('g(30)的值为：', g(30))
