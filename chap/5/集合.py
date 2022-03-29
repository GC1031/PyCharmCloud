# ☆ 柴柴
# ☆ 2022/3/12  16:44


# 集合是Python内置的数据结构，是可变的序列，是没有value的字典

'''
# 集合的创建
# 1.直接创建
a={'A','hello',100,100}             # 集合中的元素不允许重复
print(a)

# 2.使用内置函数set()
i=set(range(6))
print(i)
i1=set([1,2,3,1,3])                 # 将列表转为集合
i2=set((10,20,100,30,50,50,50))     # 将元组转为集合，集合中的元素是无序的
i3=set('hello')                     # 将字符串转为集合
i4=set({55,44,33})                  # 将集合转为集合
print(i1,i2,i3,i4)

# 3.空集合
i5=set()
print(i5)
'''




'''
# 集合元素的增删
i={10,20,30,40,50}
# 1.判断
print(10 in i)
print(100 in i)

# 2.增加                    add一次添加一个元素；pdate一次至少添加一个元素
i.add(80)
print(i)
i.update({11,22,33})
print(i)
i.update([520,526])
i.update((123,456,789))
print(i)

# 3.删除                    remove一次删除一个指定元素，不存在则KeyError；discard一次删除一个指定元素，不存在不抛出异常；
#                          pop一次删除一个任意元素；clear清空集合
i.remove(520)
print(i)
i.discard(789)
print(i)
i.pop()
i.pop()
i.pop()
print(i)
i.clear()
print(i)
'''




'''
# 集合间的关系
# 1.两个集合是否相等        元素相同就相等
a={10,20,30,40}
i={10,20,30,40}
print(a==i)

# 2.A是否是B的子集
a1={1,2,3,4,5,6,7}
i1={2,3,5}
print(i1.issubset(a1))

# 3.A是否是B的超集
print(a1.issuperset(i1))

# 4.两个集合是否没有交集
k={2,5,10,15}
print(a1.isdisjoint(k))
'''




'''
# 集合的数学操作
# 1.交集                           intersection = &
s1={1,2,3}
s2={3,4,5}
print(s1.intersection(s2))
print(s1 & s2)

# 2.并集                           union = |
print(s1.union(s2))
print(s1 | s2)

# 3.差集                           difference = -
print(s1.difference(s2))
print(s1-s2)
print(s2.difference(s1))
print(s2-s1)

# 4.对称差集                        symmetric_difference = ^
print(s1.symmetric_difference(s2))
print(s2^s1)
'''




# 集合生成式         格式：{i*i for i in range(1,10)}
a={i*i for i in range(1,10)}
print(a)