# ☆ 柴柴
# ☆ 2022/3/16  20:49

'''
# 字符串的驻留机制（交互模式 Win+R cmd）
# 1.字符串的长度为0或1时
# 2.符合标识符的字符串
# 3.字符串只在编译时进行驻留，而非运行时
# 4.[-5,256]之间的整数



# 字符串的查询
a='hEllo,hEllo'
# index()      查找子串substr第一次出现的位置，查找不到返回ValueError
print(a.index('lo'))     # 3  序号从0开始
# rindex()      查找子串substr最后一次出现的位置，查找不到返回ValueError
print(a.rindex('lo'))
# find()      查找子串substr第一次出现的位置，查找不到返回-1
print(a.find('lo'))
# rfind()      查找子串substr最后一次出现的位置，查找不到返回-1
print(a.rfind('lo'))




# 字符串的转换
# upper()         所有字符转成大写
i=a.upper()
print(i)
# lower()         所有字符转成小写
print(a.lower())
# swapcase()      大小写调换
print(a.swapcase())
# capitalize()    第一个字符大写，其余都是小写
print(a.capitalize())
# title()         每个单词第一个字符大写，剩余字符小写
print(a.title())
'''




'''
# 字符串内容的对齐操作
a='hello,python'
# center()     居中对齐，第1个参数指定宽度，第2个参数指定填充符，第2个参数可选，默认是空格，如果设置宽度小于实际宽度则返回原字符串
print(a.center(20,'*'))
# ljust()      左对齐
print(a.ljust(20))
print(a.ljust(20,'!'))
# rjust()      右对齐
print(a.rjust(20,'/'))
# zfill()      右对齐，左边用0填充，只接受一个参数，用于指定字符串的宽度
print(a.zfill(20))
print('-555'.zfill(8))
'''




'''
# 字符串的劈分
# split()         从字符串的左端开始劈分，默认劈分字符是空格，返回值是一个列表
s='hello world ahaha'
print(s.split())
#                 以通过参数sep指定劈分字符串是的劈分符
s1='hello|world|ahaha'
print(s1.split())
print(s1.split(sep='|'))
#                 通过参数maxsplit指定劈分字符串的最大劈分次数，在经过最大次劈分之后，剩余的子串会单独作为一部分
print(s1.split(sep='|',maxsplit=1))

# rsplit()        从字符串的右端开始劈分，默认劈分字符是空格，返回值是一个列表
print(s.rsplit())
print(s1.rsplit(sep='|'))
print(s1.rsplit(sep='|',maxsplit=1))
'''





'''
# 字符串的判断
# isidentifier()         判断是否是合法的标识符（字母、数字、下划线）
s='hello,world_ahaha'
print(s.isidentifier())
# isspace()              判断是否全部由空白字符组成（回车、换行、水平制表符）
print('\t'.isspace())
# isalpha()              判断是否全部由字母组成
print('嗷嗷嗷'.isalpha())
print('啊啊啊222'.isalpha())
# isdecimal()            判断是否全部由十进制的数字组成
print('123456'.isdecimal())
print('12345六'.isdecimal())
print('ⅠⅡⅢ'.isdecimal())
# isnumeric()            判断是否全部由数字组成
print('123456'.isnumeric())
print('12345六'.isnumeric())
print('ⅠⅡⅢ'.isnumeric())
# isalnum()              判断是否全部由字母和数字组成
print('aaa222'.isalnum())
print('aaa!!!'.isalnum())
'''





'''
# 字符串的替换与合并
# 替换 replace()    第1个参数指定被替换的子串，第2个参数指定替换子串的字符串，第3个参数指定最大替换次数，该方法返回替换后的字符串，不改变原字符串
s='hello,python,python,python'
print(s.replace('python','ahaha'))
print(s.replace('python','baibai',2))

# 合并 join()       将列表或元组中的字符串合并成一个字符串
lst=['hello','123','456']
print('~'.join(lst))
print(''.join(lst))

a=('hello','789')
print(''.join(a))

print('#'.join('hahaha'))       # 字符串序列
'''





'''
# 字符串的切片            字符串是不可变类型，不能增删改，切片后产生新的对象
s='hello,ahaha'
s1=s[:5]
s2=s[6:]
s3='~'
newstr=s1+s3+s2

print(s1)
print(s2)
print(newstr)

print(s[1:8:2])     # 从1开始截到8（不包含5），步长为2
print(s[::-1])      # 倒序
'''





'''
# 字符串的格式化
# 1.% 做占位符
name='gc'
age=23
print('我是%s，今年%d岁'%(name,age))

# 2.{} 做占位符
print('我是{0}，今年{1}岁'.format(name,age))

# 3.f-string
print(f'我叫{name}，今年{age}岁')
'''





'''
# 字符串的宽度和精度
print('%d' % 100)
print('%10d' % 100)        # 10表示宽度
print('%f' % 3.141592)
print('%.3f' % 3.141592)   # .3表示精度

print('%10.3f' % 3.141592) # 同时限制宽度精度

print('{0}'.format(3.141592))           # 0代表占位符次序
print('{0:.3}'.format(3.141592))        # .3表示一共3位数
print('{0:.3f}'.format(3.141592))       # .3f表示3位小数
print('{0:10.3f}'.format(3.141592))     # 同时限制宽度精度
'''







# 字符串的编码与解码           编码将字符串转为二进制数据（bytes），解码相反
s='哈哈哈哈哈哈哈'
# 编码
print(s.encode(encoding='GBK'))             # 在GBK编码格式中一个中文占两个字节
print(s.encode(encoding='UTF-8'))           # 在UTF-8编码格式中一个中文占三个字节

# 解码
byte=s.encode(encoding='GBK')               # byte代表一个二进制数据（字节类型的数据）
print(byte.decode(encoding='GBK'))

byte=s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))