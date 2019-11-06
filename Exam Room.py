class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.seats = [0] * N
        self.count = 0

    def seat(self):
        """
        :rtype: int
        """
        if self.count ==0:
            self.seats[0] = 1
        elif self.count ==1:
            self.seats[len(self.seats)-1] = 1


        self.count +=1

    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        self.seats[p] = 0
        self.count -=1
# Your ExamRoom object will be instantiated and called as such:
obj = ExamRoom(10)
print(obj.seats)
param_1 = obj.seat()
# obj.leave(p)