class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key in self.dict:
            tmp = self.dict[key]['time']
            tmp.append(timestamp)
            self.dict[key]['time'] = tmp
            tmp = self.dict[key]['value']
            tmp.append(value)
            self.dict[key]['value'] = tmp
        else:
            val ={}
            tmp=[value]
            val['value'] = tmp
            tmp = [timestamp]
            val['time'] = tmp
            self.dict[key] = val
        # print(self.dict)

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        # print(self.dict)
        if key not in self.dict or timestamp < self.dict[key]['time'][0]  :
            return ''
        elif  timestamp >= self.dict[key]['time'][-1]:
            return self.dict[key]['value'][-1]
        else:
            rtn = ''
            low = 0
            high = len(self.dict[key]['time'])
            while low <= high:
                mid = low + (high-low)//2
                if timestamp == mid:
                    return self.dict[key]['value'][mid]
                elif timestamp < self.dict[key]['time'][mid]:
                    high = mid-1
                else:
                    low = mid
            return self.dict[key]['value'][high]

            # for i in range(len(self.dict[key]['time'])):
            #     if  self.dict[key]['time'][i] <= timestamp  :
            #         rtn = self.dict[key]['value'][i]
            # return rtn




# Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
# Output: [null,null,"bar","bar",null,"bar2","bar2"]






obj = TimeMap()
obj.set("foo","bar",1)
print(obj.get("foo",1))
print(obj.get("foo",3))
obj.set("foo","bar2",4)
print(obj.get("foo",4))
print(obj.get("foo",5))

