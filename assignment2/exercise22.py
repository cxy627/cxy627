#coding:utf-8
'''
'''
dict1 = {1:"1ew",2:"dsfe",3:"vfewr23",4:"2r3ff"}

key = dict1.keys()
value = dict1.values()
zip_dict2 = zip(value,key)
dict2 = dict(zip_dict2)
print(dict2)