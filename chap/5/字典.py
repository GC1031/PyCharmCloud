# ☆ 柴柴
# ☆ 2022/3/12  9:23


# 字典以键值对的方式存储数据，是一个无序的序列，是根据key查找value所在的位置
# 格式：scores={ 'A':100 , 'B':50 , 'C':20 }

'''
# 字典的创建
# 1.使用花括号
scores={ 'A':100 , 'B':50 , 'C':20 }
print(scores)
# 2.使用内置函数dict()
i=dict(name='jack',age=20)
print(i)
# 空字典
a={}
print(a)
'''





'''
# 字典元素的获取
# 1.[]        元素不存在则抛出keyError
scores={ 'A':100 , 'B':50 , 'C':20 }
print(scores['A'])

# 2.get()     元素不存在则返回None，也可以指定返回值
print(scores.get('A'))
print(scores.get('F',250))
'''





'''
# 字典元素的增、删、改
# key的判断
scores={ 'A':100 , 'B':50 , 'C':20 }
print('A'in scores)
print('A'not in scores)

# 字典元素的删除
del scores['C']      # 删除指定的key-value对
scores.clear()       # 清空字典的所有元素
print(scores)

# 字典元素的新增
scores['E']=90
print(scores)

# 字典元素的修改
scores['E']=70
print(scores)
'''





'''
# 获取字典视图
scores={'A':100,'B':60,'C':20}
# 1.keys()        获取字典中所有key
i=scores.keys()
print((i))
print(list(i))      # 将所有key组成的视图转成列表

# 2.values()      获取字典中所有value
a=scores.values()
print((a))
print(list(a))

# 3.items()       获取字典中所有key-value对
k=scores.items()
print(k)
print(list(k))      # 转换之后的列表元素由元组构成
'''





'''
# 字典元素的遍历
scores={'A':100,'B':50,'C':0}
for i in scores :
    print(i,scores[i],scores.get(i))
'''





# 字典的特点
# 1.字典中所有元素都是key-value对，key不可重复
# 2.字典中的元素是无序的
# 3.字典中的key必须是不可变对象
# 4.字典可以根据需要动态伸缩
# 5.字典占内存较大，是一种使用空间换时间的数据结构





# 字典生成式
items=['A','B','C','D']
prices=[100,60,20,0]
i={ item:price  for item,price in zip(items,prices) }
print(i)