class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        lgt = len(citations)
        running = [0]* (lgt+1)

        for each in citations:
            if each >= lgt:
                running[lgt] +=1
            else:
                running[each] +=1
        # print(running)
        curr = 0
        for i in range(lgt, -1, -1):
            curr +=running[i]
            # print(i, curr)
            if curr>=i:
                return i









citations = [3,0,6,1,5]
sol = Solution()
print(sol.hIndex(citations))