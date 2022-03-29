# ☆ 柴柴
# ☆ 2022/3/9  21:38

# range()的三种创建方式
'''
range(stop)                      range(10)
range(start,stop)                range(1,10)
range(start,stop,step)           range(1,10,2)
'''
'''
r=range(10)
x=range(1,10)
y=range(1,10,2)
print(list(r))
print(list(x))
print(list(y))
print(10 not in list(y))
'''





# while
'''
a=0
while a<5 :
    print(a)
    a+=1
'''
''' #计算0-4的和
a=0
s=0
while a<5 :
    s+=a
    a+=1
print(s)
'''
'''
# 计算1-100之间的偶数和
a=1
s=0
while a<=100 :
    if a%2==0 :
        s+=a
    a+=1
print(s)
'''




# for  in
'''
for item in 'python' :
    print(item)
'''
'''
for i in range(3) :
    print('12345')
'''
'''
# 计算1-100之间的偶数和
s=0
for i in range(0,101,2):
    s+=i
print(s)
'''
'''
# 计算100-999之间的水仙花数
for i in range(100,1000) :
    a=i % 10
    b=i //10 % 10
    c=i // 100
    if i==a**3+b**3+c**3 :
        print(i)
'''





# break
'''
# 从键盘录入密码，最多录入3次，正确就结束循环
for i in range(3) :
    a=input('请输入密码：')
    if a=='888':
        print('密码正确')
        break
    else:
        print('密码错误')
'''




# continue
'''
# 输出1-50之间所有5的倍数
for i in range(1,51):
    if i % 5 != 0 :
        continue
    print(i)
'''




# else    循环中没有遇到break就执行else
'''
# 从键盘录入密码，最多录入3次，正确就结束循环
for i in range(3) :
    a=input('请输入密码：')
    if a=='888':
        print('密码正确')
        break
    else:
        print('密码错误')
else:
    print('三次机会已使用完')
'''






# 嵌套
'''
# 输出三行四列的矩形
for i in range(1,4) :                # 行数
    for j in range (1,5) :           # 列数
        print('*',end='\t')          # 不换行输出
    print()                          # 换行
'''

# 输出九九乘法表
for i in range(1,10):
    for j in range (1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print()