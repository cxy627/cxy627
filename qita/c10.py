a=[1,2,3,4,5,6,7,8]

# # for i in range(0,len(a),2):
# #     print(a[i],end='|')

b = a[len(a):-len(a):-2]

# 高性能，封装性（复用性）

print(b)