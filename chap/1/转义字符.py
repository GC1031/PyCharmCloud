# ☆ 柴柴
# ☆ 2021/8/16  14:52

# \n 换行 --> newline
# \t 水平制表符 4个字符
# \r 覆盖 --> return 后面将前面覆盖
# \b 退格 --> back 把前面一个字符退没了

print('hello\nworld')
print('hello\tworld')
print('helloooo\tworld')
print('hello\rworld')
print('hello\bworld')


print('http:\\\\www.baidu.com')     # 两个\输出后转成一个
print('他说：\"我爱你\"')             # 输出内容中包含”“ ‘’，用\进行标记


# 原字符：不希望字符串中的转义字符起作用，在字符串前加r或R     最后一个字符不能是单个的\，否则报错
print(r'hello\nworld')
print(r'hello\nworld\\')