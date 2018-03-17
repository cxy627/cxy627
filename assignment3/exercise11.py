# coding:utf-8
'''
'''


def unionmap(list1, list2, func=lambda x, y: (x, y)):
    return list(map(func, list1, list2))


def unionzip(list1, list2):
    return list(zip(list1, list2))


if __name__ == "__main__":
    print(unionmap([1, 2, 3], ['u', 'ee', 'wdew']))
    print(unionzip([1, 2, 3], ['u', 'ee', 'wdew']))
