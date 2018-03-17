# coding:utf-8
'''
补充题2
'''
lst = {"奴隶社会": {"亚洲": {"古印度": ["种姓制度", "佛教的创立"], "两河流域文明": ["汉谟拉比法典"]}, "欧洲": {"希腊罗马古典文化": [
    "建筑艺术", "公历"], "罗马": ["城邦", "帝国的征服与扩展"], "希腊": ["希腊城邦", "雅典民主"]}, "非洲": {"古埃及文明": ["金字塔"]}}}


def outlist(lst):
    if type(lst) == dict:
        for key in lst:
            print(key)
            # print(key)
            yield key
            for in_  key in outlist(lst[key]):
                print(in_key)
                # yield in_key
    else:
        for item in lst:
            pass
        #     yield item
        # yield "strip"
        for key in lst:
            # print(key)
            yield key
            print(key)

print(list(outlist(lst)))

    
