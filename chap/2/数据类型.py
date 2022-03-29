# ☆ 柴柴
# ☆ 2021/8/16  16:07

# int --> 整数 23
# float--> 浮点数 3.14159
# bool --> 布尔 True，False
# str --> 字符串 阿巴阿巴阿巴

# 整数
a=250
b=-125
c=0
print(a,type(a),'\n',b,type(b),'\n',c,type(c))

print('十进制',22)             # 默认
print('二进制',0b1001001)      # 0b
print('八进制',0o176)          # 0o
print('十六进制',0x879F)        # 0x



# 浮点数
a=1.1
b=2.2
print(a+b)      # 直接计算有错误

from decimal import Decimal         # 导入Decimal模块
print(Decimal('1.1')+Decimal('2.2'))



# 布尔  True=1  False=0
f1=True
f2=False
print(f1,f2,f1+f2)



# 字符串
str1='早日暴富'
str2="日进斗金"
str3="""大吉
大利"""

print(str1,str2,'\n',str3)



# 数据类型转换
name='维尼'
age=22
print(name,age)
#print('我叫'+name+'，今年'+age+'岁')         # 报错
print('我叫'+name+'，今年'+str(age)+'岁')     # 类型转换
print('我叫',name,'，今年',age,'岁')          # ,增加句中空格



# 语句注释
# Ctrl+/    快速注释
'''嘿嘿
三引号是多行注释'''