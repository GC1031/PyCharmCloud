# ☆ 柴柴
# ☆ 2022/3/10  15:47
'''
# 列表的创建
# 1.使用中括号
lst=['hello','world',555]
# 2.使用内置函数list()
lst2=list(['hello','world',666])



# 列表的特点
# 1.列表元素按顺序有序排序
print(lst)
# 2.索引映射唯一个数据(正向索引为0 1 2，逆向索引为-1 -2 -3）
print(lst[0],lst[-3])
# 3.列表可以存储重复数据
# 4.任意数据类型混存
# 5.根据需要动态分配和回收内存
'''






'''
# 列表的查询
lst=['hello','world','!',123,'hello']
# 1.获取列表中的指定元素      索引 index()
# 如果列表中存在N个相同元素，只返回相同元素中的第一个元素的索引
print(lst.index('hello'))
# 如果查询的元素在列表中不存在，则会抛出ValueError
# 可以在指定的start和stop之间进行查找   范围为[)
print(lst.index('!',1,3))




# 2.获取列表中的单个元素
# 正向索引从0到N-1
print(lst[2])
# 逆向索引从-N到-1
print(lst[-2])
# 指定索引不存在则抛出ValueError




lst2=[10,20,30,40,50,60,70,80]
# 3.获取列表中的多个元素      切片操作      语法格式：列表名[start:stop:step]
# step默认为1,可简写为[start:stop]
print(lst2[0:3])

# step为正数，从start开始往后计算切片。
print(lst2[::1])
#           [:stop:step]  切片的第一个元素默认是列表的第一个元素
print(lst2[:4:2])
#           [start::step] 切片的最后一个元素默认是列表的最后一个元素
print(lst2[2::2])

# step为负数，从start开始往前计算切片。
print(lst2[::-1])
#           [:stop:step]  切片的第一个元素默认是列表的最后一个元素
print(lst2[:0:-2])
#           [start::step] 切片的最后一个元素默认是列表的第一个元素
print(lst2[6::-2])




# 4.判断指定元素在列表中是否存在        in、not in
print('p' in 'python')
print('o' not in 'python')
print(20 in lst)
print('world' in lst)
'''




'''
# 列表元素的遍历
lst=[10,20,'hello']
for item in lst:
    print(item)
'''




'''
# 列表元素的增删改
# 1.增加     append()在末尾添加一个元素；extend()在末尾至少添加一个元素；insert()在任意位置添加一个元素；切片 在任意位置至少添加一个元素
lst=[1,2,3]
lst.append('haha')
print(lst)

lst2=[789,'hello']
# lst.append(lst2)      # 将lst2作为一个整体的元素添加到列表的末尾
lst.extend(lst2)
print(lst)

lst.insert(1,'wow')
print(lst)

lst3=['ipad','mac','iphone']      # 切片是从某个位置开始插入元素，元列表该位置后的所有元素被舍弃，相当于覆盖
lst[2:]=lst3
print(lst)
'''

'''
# 2.删除     remove()一次删除一个元素、重复元素只删除第一个、元素不存在则ValueError；
#           pop()删除一个指定索引位置上的元素、不指定索引则删除最后一个元素、指定索引不存在则ValueError；
#           切片 一次至少删除一个元素；
#           clear()清空列表；del删除列表
lst=[1,2,3,4,5,3]
lst.remove(3)
print(lst)

lst.pop(1)
print(lst)
lst.pop()
print(lst)

new_list=lst[1:2]       # 此处是切出来的新列表，相当于从原列表中提取出了一部分，产生新的列表对象
print(new_list)

lst[1:2]=[]             # 此处是用一个空列表替代需要删除的部分，从而不产生新的列表对象并删除原列表指定内容
print(lst)

lst.clear()
print(lst)

del lst
# print(lst)       NameError: name 'lst' is not defined
'''

'''
# 3.修改
lst=[1,2,3,4]
# 一次修改一个值
lst[2]=555
print(lst)
# 切片修改
lst[2:3]=[7,8,9,10,11,12]
print(lst)
'''





'''
# 列表排序
# 1.调用sort（）方法           不改变原列表id
lst=[55,12,79,63,48]
lst.sort()                   # 默认升序，从小到大排序
print(lst)
lst.sort(reverse=True)       # 指定reverse=True可以降序排序
print(lst)

# 2.调用内置函数sorted()       改变原列表id，产生新的列表对象
lst2=[55,12,79,63,48,100]
new_list=sorted(lst2)                    # 升序
print(new_list)
new_list2=sorted(lst2,reverse=True)      # 降序
print(new_list2)
'''




# 列表生成式（生成列表的公式）
# 格式：[i*i for i in range(1,10)]       i*i是列表元素的表达式/通项公式；i是自定义变量；range(1,10)是可迭代对象
lst=[i for i in range(1,10)]
print(lst)
lst2=[a**2+1 for a in range(1,5)]
print(lst2)
lst3=[i*2 for i in range(1,6)]
print(lst3)