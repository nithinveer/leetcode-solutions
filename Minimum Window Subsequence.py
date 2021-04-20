class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        
        # I would be using Two Pointer approach
        # First ensure your T is in S and 
        # set the index where the last char of T is seen in S as second
        # Now move back one char by char and get the first in S
        # where first is the index position of T[0] in S
        # Once you find, make comparision and update your answer(rtn) accordingly
        
        rtn = ''
        maxi = float('inf')
        tIdx = first = 0
        while first < len(S) :
            if S[first] == T[tIdx]:
                tIdx +=1 # Move the tIdx 
            if tIdx == len(T):
                # This is where we know T is present in subset of S
                # So set the second pointer
                second = first
                tIdx -=1
                # Now pass back in the S to find the starting point which is First
                while tIdx >=0:
                    if T[tIdx] == S[first]:
                        tIdx -=1
                    first -=1
                first +=1
                tIdx +=1                
                
                # Compariosn 
                if second - first +1 < maxi :
                    maxi = second - first
                    rtn = S[first:second+1]
            first+=1
                        
        
        return rtn