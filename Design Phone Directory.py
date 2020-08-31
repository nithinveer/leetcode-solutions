from collections import deque
class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.nums = deque()
        for i in range(maxNumbers):
            self.nums.append(i)
        self.used = set()


    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        if len(self.nums) == 0:
            return -1
        poped = self.nums.popleft()
        self.used.add(poped)
        return poped

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return not(number in self.used)

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: None
        """
        if number in self.used:
            self.used.remove(number)
            self.nums.append(number)

