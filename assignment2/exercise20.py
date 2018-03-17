#coding:utf-8

'''
'''

dict1 = {"w":92,"k":93,"iw":827,"wxw":92873,"q":8728}
print(sorted(dict1.keys()))
print([(key,dict1[key])for key in sorted(dict1.keys())])
print(sorted(dict1.items(), key=lambda item:item[1]))