class Solution(object):
    def fair(self, slots):
        slots.sort(key=lambda  x: x[1])
        self.slots = slots
        n = len(slots)
        dp = [0] * (n + 1)
        for i, slot in enumerate(slots):
            s, e = slot[0], slot[1]
            dp[i+1] = 1
            for j in range(i, -1, -1):
                if slots[j][1]<=s:
                    dp[i+1] = max(dp[i], dp[j+1]+1 )
                    break
            dp[i+1] = max(dp[i], dp[i+1])
        return dp[-1]





if __name__ == '__main__':
    sol = Solution()
    print(sol.fair([[1,11],[1,4],[1,7],[1,5],[5,10], [4,6], [7,12]]))