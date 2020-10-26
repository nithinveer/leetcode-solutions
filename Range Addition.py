class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        rtn = [0]*length 
        if not updates :
            return rtn
        periods = []
        
        for update in updates :
            periods.append([update[0], update[2]])
            periods.append([update[1]+1, -update[2]])
        periods.sort(key=lambda x:x[0])
        piv = 0
        
        inc = 0
        for index in range(length):
            while piv < len(periods) and index == periods[piv][0]:
                inc += periods[piv][1]
                piv +=1
            rtn[index] = inc
        return rtn
            