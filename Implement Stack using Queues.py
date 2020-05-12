class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = []
    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.lst.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.lst.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.lst[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if len(self.lst) == 0:
            return True
        return False
