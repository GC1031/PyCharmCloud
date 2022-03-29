# ☆ 柴柴
# ☆ 2022/3/9  20:47

# 单分支
'''
sum=100
a=int(input('请输入取款金额：'))
if a<=sum :
    sum-=a
    print('取款成功，余额：',sum,'元')
'''




# 双分支
'''
a=int(input('请输入一个整数：'))
if a % 2 == 0 :
    print(a,'是偶数')
else:
    print(a,'是奇数')
'''




# 多分支
'''
90-100 A    80-89 B    70-79 C    60-69 D    0-59 E    小于0或大于100为非法数据
'''
'''
i=int(input('请输入成绩：'))
if 90 <= i <= 100 :
    print('A')
elif 80 <= i <= 89:
    print('B')
elif 70 <= i <= 79 :
    print('C')
elif 60 <= i <= 69 :
    print('D')
elif 0 <= i <= 59 :
    print('E')
else:
    print('请输入正确的数字')
'''




# 嵌套
'''
会员 >=200 打8折   >=100 打9折   非会员 >=200 打9.5折
'''
'''
i=int(input('是否会员（是输入1，否输入0）：'))
a=float(input('请输入消费金额：'))
if i == 1 :
    if a>=200 :
        print('需付款：',a*0.8,'元')
    elif 100<=a<200 :
        print('需付款：',a*0.9,'元')
    else:
        print('需付款：',a,'元')
else:
    if a>=200 :
        print('需付款：',a*0.95,'元')
    else:
        print('需付款：',a,'元')
'''




# 使用条件表达式比较两数大小
a=int(input('请输入第一个整数：'))
b=int(input('请输入第一个整数：'))
'''
if a>=b :
    print(a,'>=',b)
else:
    print(a,'<',b)
'''

print( (str(a)+'>='+str(b))     if a>=b else     (str(a)+'<'+str(b)) )





# pass语句，只是一个占位符
'''
if a==0 :
    pass
else:
    pass
'''