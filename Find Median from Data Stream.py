import heapq


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l1 = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.l1.append(num)

    def findMedian(self):
        """
        :rtype: float
        """
        heapq.heapify(self.l1)
        # print(self.l1)
        if len(self.l1) % 2 == 0:
            # print('even')
            # print(int(len(self.l1) / 2), int(len(self.l1) / 2 - 1))
            print(int((self.l1[int(len(self.l1) / 2)] + self.l1[int(len(self.l1) / 2 - 1)]) / 2) +0.5 )
            if int((self.l1[int(len(self.l1) / 2)] + self.l1[int(len(self.l1) / 2 - 1)]) / 2) %2 ==1:
                return int((self.l1[int(len(self.l1) / 2)] + self.l1[int(len(self.l1) / 2 - 1)]) / 2) + 0.5
            else :
                return int((self.l1[int(len(self.l1) / 2)] + self.l1[int(len(self.l1) / 2 - 1)]) / 2)

        else:
            # print('odd')
            return (self.l1[int(len(self.l1) / 2)])

if __name__ == '__main__':
    med  = MedianFinder()
    med.addNum(1)
    med.addNum(2)
    med.findMedian()
    med.addNum(3)
    med.findMedian()
