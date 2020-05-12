class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.first = []
        self.second = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.first.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.second) > 0:
            return self.second.pop()
        else:
            while len(self.first)> 0 :
                self.second.append(self.first.pop())

        return self.second.pop()


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.second) > 0:
            return self.second[-1]
        else:
            return self.first[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.first) ==0 and len(self.second) == 0:
            return True
        else:
            return False



# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
print(obj.empty())
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.pop())
print(obj.empty())
print(obj.peek())
obj.push(4)
print(obj.pop())
print(obj.peek())
obj.push(5)
print(obj.peek())
print(obj.empty())