# ☆ 柴柴
# ☆ 2021/8/16  14:52

# 数据输出到文件中
# 1.盘符要存在   2.使用file=fp   3.a+表示如果文件不存在就创建，存在就在文件内容后继续追加
fp = open ('G:/bilipy/python 0.1.txt','a+')
print ('https://www.runoob.com/w3cnote/pycharm-windows-install.html',file=fp)
fp.close()