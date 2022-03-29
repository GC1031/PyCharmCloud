# ☆ 柴柴
# ☆ 2022/3/29  23:37


'''
# 函数的创建和调用
# 1.实现代码的复用     2.隐藏程序实现的细节    3.提高程序的可维护性     4.提高代码的可读性，便于调试

# def 函数名 ([输入参数]):
#     函数体
#     [return xxx]

def calc(a,b):                           # a b 为形参，位置在函数的定义处
    c=a+b
    return c

m=int(input('请输入第一个数：'))            # 输入的数值为实参，位置在函数的调用处
n=int(input('请输入第二个数：'))
i=calc(m,n)
print(i)
'''



'''
# 函数的参数传递
def calc(a,b):
    c=a+b
    return c

# 位置实参              根据形参对应的位置进行实参传递
i=calc(10,20)
print(i)

# 关键字实参             根据形参名称进行实参传递，=左边的变量名称即为关键字实参
i=calc(b=50,a=30)
print(i)



def fun(m,n):
    print('m=',m)
    print('n=',n)
    m=100
    n.append(10)
    print('m=',m)
    print('n=',n)

a=50
b=[1,2,3]
print('a',a)
print('b',b)
fun(a,b)
print('a',a)              # 如果是不可变对象（字符串、元组），函数体的修改不影响实参的值      m改为100，不影响实参a
print('b',b)              # 如果是可变对象（列表、字典），函数体的修改影响实参的值           n的append(10)，影响b
'''





'''
# 函数的返回值
# 如果函数没有返回值（函数执行完毕后不需要给调用处提供数据），return可以省略
# 函数的返回值如果是1个，则直接返回原类型；如果是多个，则返回元组
def fun(num):
    odd=[]
    even=[]
    for i in num:
        if i%2:                     # 0的bool值为false，非0为true
            odd.append(i)
        else:
            even.append(i)
    return odd,even

print(fun([10,21,32,43,54,65,76,87,98]))




def fun1():
    print('hello')

fun1()




def fun2():
    return 'world'

print(fun2())




def fun3():
    return 'apple','orange','peer'

print(fun3())
'''





'''
# 函数的参数定义
# 函数定义默认值参数：函数定义时，给形参设置默认值，只有与默认值不符的时候才需要传递实参
def fun(a,b=10):
    print(a,b)

fun(100)            # 只传1个参数，b使用默认值
fun(100,200)        # 实参替换形参




# 个数可变的位置参数：无法事先确定传递的位置实参的个数，使用*定义个数可变的位置形参，结果为一个元组
def fun1(*m):
    print(m)

fun1(1)          # 元组只有一个元素时会有','
fun1(1,2)
fun1(1,2,3)

# def fun3(*m,*n):          会报错，可变的位置参数只能有1个




# 个数可变的关键字参数：无法事先确定传递的关键字实参的个数，使用**定义个数可变的关键字形参，结果为一个字典
def fun2(**m):
    print(m)

fun2(a=10)
fun2(a=10,b=20,c=30)

# def fun3(**m,**n):        会报错，可变的关键字参数只能有1个




# 在一个函数的定义过程中，当既有个数可变的位置形参也有个数可变的关键字形参时，个数可变的位置形参需要放在个数可变的关键字形参之前
# def fun3(*m,**n):
# def fun3(**m,*n):       报错
'''





'''
def fun(a,b,c):
    print('a=',a)
    print('b=',b)
    print('c=',c)

fun(10,20,30)
lst=[40,50,60]
fun(*lst)                   # 函数调用时将列表中的每个元素都转换为位置实参传入

fun(a=100,b=200,c=300)
dic={'a':111,'b':222,'c':333}
fun(**dic)                 # 函数调用时将字典中的每个元素都转换为关键字实参传入






def fun1(a,b,*,c,d):       # 从*之后的参数只能采用关键字实参传递
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)

fun1(10,20,c=30,d=40)
'''






'''
# 变量的作用域
def fun(a,b):
    c=a+b              # a b c都是局部变量，是在函数体内进行定义的变量，只在函数内起作用
    print(c)
fun(5,5)


age=20                 # age是全局变量
def fun1():
    print(age)
fun1()


def fun2():
    global i           # 将函数内部的局部变量 i 转变为全局变量
    i = 100
    print(i)
fun2()
print(i)
'''








# 递归函数————在函数体内调用该函数本身
# 组成部分：递归调用和递归终止的条件
# 调用过程：每递归调用一次函数都会在栈内存分配一个栈帧；每执行完一次函数都会释放相应的空间
# 优点：思路和代码简单
# 缺点：占用内存多，效率低
'''
# 阶乘
def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)
print(fac(5))
'''
'''
# 斐波那契数列
def fib(n):
    if n<3:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(6))                           # 计算第6位的数值
for i in range(1,7):                    # 输出前6位
    print(fib(i))
'''

a=b=1
for i in range(1,7):
    if i<3:
        print('1')
    else:
        sum=a+b
        a=b
        b=sum
        print(sum)