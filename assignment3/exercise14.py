# coding:utf-8
'''
习题11-10
'''

import os
floder = r'C:\\'
files = filter(lambda x: x and x[0] != '.', os.listdir(floder))
print(list(files))
# 应该是去除以.作为开头的文件，我认为具体的作用是在unix系统下显示
# 所有该目录的文件的列表，而不包含父目录和当前目录
