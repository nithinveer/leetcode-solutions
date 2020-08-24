class UndergroundSystem(object):

    def __init__(self):
        self.journey = {}
        self.avg = {}




    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        # obj = []
        # obj.append(stationName, t)
        self.journey[id] =[stationName, t]


    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        if self.journey[id][0]+'#'+stationName in self.avg:
            avg_time = self.avg[self.journey[id][0]+'#'+stationName][0] + t-self.journey[id][1]
            self.avg[self.journey[id][0] + '#' + stationName] = (avg_time,self.avg[self.journey[id][0]+'#'+stationName][1]+1 )
        else:
            avg_time  = t - self.journey[id][1]
            self.avg[self.journey[id][0] + '#' + stationName] = (avg_time,  1)
        # print(self.avg)

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        # print(self.avg)
        time, num = self.avg[startStation + '#' + endStation]
        return time/num

# Your UndergroundSystem object will be instantiated and called as such:

obj = UndergroundSystem()
print(obj.checkIn(10, "Leyton", 3))
print(obj.checkOut(10, "Paradise", 8))
print(obj.getAverageTime("Leyton", "Paradise"))
print(obj.checkIn(5, "Leyton", 10))
print(obj.checkOut(5, "Paradise", 16))
print(obj.getAverageTime("Leyton", "Paradise"))
print(obj.checkIn(2, "Leyton", 21))
print(obj.checkOut(2, "Paradise", 30))
print(obj.getAverageTime("Leyton", "Paradise"))
# print(obj.getAverageTime("Leyton","Waterloo"))
# print(obj.checkOut(10,"Waterloo",38))
# print(obj.getAverageTime("Leyton","Waterloo"))
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)