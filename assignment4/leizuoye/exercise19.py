#这个题目好像本身已经会引起typeerror，少了参数的输入,下面的分析基于已解决该问题
# 这么写应该是会引起死循环，等于是在无限的迭代sortedkeydict类的keys自身。
# 并没有在引用父类的keys方法，至于如何顺利工作，首先要加入，要么使用super方法返回父类对象
#要么直接写sorted(dict.keys())直接引用，或者直接不写keys方法，写__getattr__(self,attr_name)
#判断attr_name如果等于keys，则返回sortred(getattr(输入字典对象,attr_name))
