class Solution(object):
    def minCostold(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        rtn = 0
        
        def remove(i,j):
            odd = 0
            even = 0
            for p in range(i, j+1):
                if p%2==0:
                    even += cost[p]
                else:
                    odd += cost[p]
            return min(odd, even)

        l = 0
        r = 0
        last = s[0]
        for i in range(1, len(cost)):
            if s[i] == last:
                r+=1
            else:
                if l != r:
                    rtn +=remove(l,r)
                last = s[i]
                l = i
                r = i
        if l != r:
            rtn += remove(l, r)
        return rtn
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        rtn = 0
        stack = []
        stack.append([s[0],0])
        for i in range(1, len(cost)):
            if stack and stack[-1][0] == s[i]:
                # print(i)
                if cost[stack[-1][1]] < cost[i]:
                    rtn +=cost[stack[-1][1]]
                    stack.pop()
                    stack.append([s[i], i])
                else:
                    rtn += cost[i]
            else:
                stack.append([s[i], i])
            # print(i,rtn)
        return rtn


s = "aabaa"
cost = [1,2,3,4,1]
# cost = [4,9,3,8,8,9]
sol = Solution()
print(sol.minCost(s, cost))