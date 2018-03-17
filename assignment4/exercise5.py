import pickle

with open('abc.pkl', 'wb') as f:
    dic = {'age': 23, 'job': 'student'}
    pickle.dump(dic, f)
# 反序列化
with open('abc.pkl', 'rb') as f:
    aa = pickle.load(f)
    print(aa)
    print(type(aa))  # <class 'dict'>