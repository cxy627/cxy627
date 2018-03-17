'''
    4
    一段小程序
'''

ACCOUNT = 'qiyue'
PASSWORD = '123456'

print('please input account')
USER_ACCOUNT = input()

print('please input password')
USER_PASSWORD = input()

if (ACCOUNT == USER_ACCOUNT)\
and (PASSWORD == USER_PASSWORD):
    print('succsed')
else:
    print('fail')
