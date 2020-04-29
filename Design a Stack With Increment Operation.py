class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.index = 0
        self.lst = [-1]*maxSize

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.index < len(self.lst):
            self.lst[self.index] = x
            self.index +=1


    def pop(self):
        """
        :rtype: int
        """
        if self.index == 0:
            return -1
        else:
            rtn_val = self.lst[self.index-1]
            self.lst[self.index-1] = -1
            self.index -= 1
            return rtn_val

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        if self.index <= k:
            for i in range(self.index):
                self.lst[i] +=val
        else:
            for i in range(k):
                self.lst[i] +=val


customStack = CustomStack(3)
print(customStack.lst)
customStack.push(1)
print(customStack.lst)
customStack.push(2)
print(customStack.lst, customStack.index)
print(customStack.pop())
print(customStack.lst)
customStack.push(2)
print(customStack.lst)
customStack.push(3)
print(customStack.lst)
customStack.push(4)
print(customStack.lst)
customStack.increment(5, 100)
print(customStack.lst)
customStack.increment(2, 100)
print(customStack.lst)
customStack.pop()
print(customStack.lst)
customStack.pop()
print(customStack.lst)
customStack.pop()
print(customStack.lst)
customStack.pop()
print(customStack.lst)