# ☆ 柴柴
# ☆ 2021/11/21  22:43

# 算术运算符
'''
print(1+1)
print(3-2)
print(2*3)
print(5/2)     #除法
print(5//2)    #整除
print(5%2)     #取余
print(2**3)    #幂运算
'''

# 复杂情况
'''
print(9//-4)    #一正一负的整除，向下取整数
print(-9//4)

print(9%-4)     #余数=被除数-除数*商  9-(-4)*(-3)=-3
print(-9%4)     #                 -9-4*(-3)=3
'''





# 赋值运算符
'''
a=b=c=20   #链式赋值
print(a,id(a),b,id(b),c,id(c))    #id是变量在内存中的位置

a=20
a+=30      #参数赋值
print(a)

a,b,c=10,20,30  #系列解包赋值
print(a,b,c)
#a,b=10,20,30  #报错，因为变量个数和值的个数不对应

#交换两个变量的值
a,b=10,20
print('交换之前：',a,b)
a,b=b,a
print('交换之后：',a,b)
'''





# 比较运算符    结果为bool类型
'''
a,b=10,20
print('a>b吗？',a>b)
print('a≠b吗？',a!=b)

#==比较的是对象的值，is比较的是对象的标识
x,y=20,20
print(a==b,x==y)
print(a is b,x is y,x is not y)
'''






#布尔运算符
'''
# and 全真为真，有假则假
a,b=10,20
print(a==10 and b==20)
print(a==10 and b>=30)

# or 有真则真
print(a==10 or b>=30)

#not 对bool类型的操作数取反
i=True
print(not i)

# in 与 not in
str='abcdefg'
print('k' in str)
print('a' in str)
'''







#位运算符   将数据转成二进制
'''
# & 对应数位都是1，结果位数则为1，否则为0
print(4&8)
print(4&4)
# | 对应数位都是0，结果位数则为0，否则为1
print(4|8)
# << 左移位，高位溢出，低位补0，向左移动一位相当于*2
print(4<<2)     #向左移动2位
# << 右移位，高位补0，低位截断，向右移动一位相当于/2
print(4>>1)
'''






#运算符的优先级
'''  有括号先算括号里的
① 幂运算 --> 乘除 --> 加减     （算术运算符）
② << >> --> & --> |         （位运算符）
③ > < >= <= == !=           （比较运算符）
④ and --> or                （布尔运算符）
⑤ =                         （赋值运算符）
'''


