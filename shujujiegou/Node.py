class Node(object):
    def __init__(self, initdate):
        self.data = initdate
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setDate(self, data):
        self.data = data

    def setNext(self, nextNode):
        self.next = nextNode
