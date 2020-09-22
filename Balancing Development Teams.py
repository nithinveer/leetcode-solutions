class Solution(object):
    def maxBalancedTeams(self, developers, maxNewHires):
        developers.sort(reverse=True)
        piv = running = rtn = 0
        while running < len(developers):
            if developers[piv] - developers[running] <= maxNewHires:
                maxNewHires -= (developers[piv] - developers[running])
                running += 1
            else:
                running -= 1
                rtn = max(rtn, (running - piv + 1))
                if piv + 1 < len(developers):
                    maxNewHires += (developers[piv] - developers[piv + 1]) * (running - piv)
                    piv += 1
                    running = max(running + 1, piv)
        rtn = max(rtn, (running - piv))
        return rtn




sol = Solution()
developers = [29, 10, 8, 9, 7, 5, 5, 3, 2, 2, 1]
maxi = 8
print(sol.maxBalancedTeams(developers, maxi))
