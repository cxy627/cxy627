#coding:utf-8
'''
习题1:
items = ( ( 3 , 2 ) , ( 5 , 7 ) , ( 1 , 9 ) , 0 , ( 1 ) ) 
（1）len(items)长度为5
（2）items[1]为从左至右第二个元素(5,7)
（3）调用items[3][0]typeerror的原因
    items[3]为int类型,不支持索引号调用该方法
（4）items[x][y]咋调到9这个数字
    X为2，y为1
（5）items[0]items[4]分别是啥类型，为啥[4]不是元组,咋把他变成元组
    分别是type(items[0]) == tuple;type(item[4]) == int。因为[4]只有一个元素，
    所以是整型。加个工厂函数强制转换就好tuple((1))或(1,)

 习题2:
 Which of the following are types mutable and which are immutable:
   int, list, ﬂoat, tuple, str.
 All the types listed are mutable except for tuple and str.
 答：应该是问哪些是可变类型哪些不是。元组,整型，字符串，浮点数为不可变类型。
    字典，列表为可变类型

习题3：
 What are the types of variables a and b in the following code:
    a=(1)  b= (1,)
答：下面两者分别是哪种类型。分别为整型，以及元组（包含元素只有1）

习题4:
What is the types and value of y after executing the following code:
 x= [1,2,3,4,5]  y=x[:] Both x and y are lists.
 They have the same value, which is [1, 2, 3, 4, 5].
 答：下面这句话是答案,均为列表，因为切片操作数值空缺代表从头至尾取值，因此
    还是[1, 2, 3, 4, 5]

习题5：
 Examine the following code: a = 10 b = 20 
 print "Before swapping a=%d, b=%d" % ( a , b ) 
 #Swap values a=b b=a print "After swapping a=%d, b=%d" % ( a , b )
 答:运行结果:%d是有符号的十进制数，因此Before swapping a=10, b=20;
    After swapping a=20, b=20
    (1)a = b =20 ,b = a =20
    (2)因为是将b的值先赋值给a，再将a的值赋值给b。
    (3)如要交换应该是a,b = b,a

习题6：
与python有关的三个属性分别是什么?
答：以对象a为例，分别为id(a)身份，type(a)类型，value(a)值

习题7：
type()是干什么的，返回值是什么？
答：是一种对象类型的查询方法,返回值是该引用对象的类型

习题8：str()和repr() 有什么区别:
答：str()把对象的数值转换为字符串，repr()也是。但前者是转换为人类易读的方式，
后者则是为解释器直接读取的形式。所以平常str()更易阅读，但如果要可逆转换repr()
更为合适。

习题9：
对象相等，type(a) == type(b) ，type(a) is type(b)有什么不同?
一个是对数值的判断，只要表达的数值一样就行
一个是对id身份的判断，引用来自一个对象实体才行。
将一个对象深拷贝后尽管值一样，但id不一样了,于是==是True,is是False
'''
