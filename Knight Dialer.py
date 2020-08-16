class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        dct = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4],
               0: [4, 6]}
        current = [1]* 10
        
        for hop in range(N-1):
            next = [0]*10
            for i in range(10):
                for each_ in dct[i]:
                    next[each_] += current[i]
            current = next

        return sum(current) % (10 ** 9 + 7)



sol  = Solution()
print(sol.knightDialer(2))