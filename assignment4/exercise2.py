from collections import Iterable
class STgetitem:

    def __init__(self, text):
        self.text = text

    def __getitem__(self, index):
        result = self.text[index].upper()
        return result


p = STgetitem("黄哥Python")
print(isinstance(p,Iterable))
print(p[0])
print("------------------------")
for char in p:
    print(char)
    print(type(char))
    print(isinstance(char,Iterable))
