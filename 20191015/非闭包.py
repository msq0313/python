def outer(): #定义函数outer
    x=10 #定义局部变量x并赋为10
    def inner(): #在outer函数中定义嵌套函数inner
        x=20 #将x赋为20
        print('inner函数中的x值为：',x)
    inner() #在outer函数中调用inner函数
    print('outer函数中的x值为：',x)
outer() #调用outer函数