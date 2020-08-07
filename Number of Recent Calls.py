class RecentCounter(object):

    def __init__(self):
        self.lst = []
        self.pivot = 0

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        if len(self.lst) == 0:
            self.lst.append(t)
            self.pivot = 0
            return 1
        else:
            while self.pivot < len(self.lst) :
                if t - self.lst[self.pivot] >3000:
                    self.pivot +=1

                else:
                    break
            self.lst.append(t)
            return len(self.lst)- self.pivot

obj = RecentCounter()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3000))
print(obj.ping(3001))
print(obj.ping(3002))
print(obj.ping(3003))
print(obj.ping(3004))