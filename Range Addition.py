class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        rtn = [0]*length 
        
        for update in updates :
            rtn[update[0]] += update[2]
            if update[1]+1 < length:
                rtn[update[1]+1] -= update[2]
        
        val = 0
        for index in range(length):
            val += rtn[index]
            rtn[index] = val
        return rtn
            
            