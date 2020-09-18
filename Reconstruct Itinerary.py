from collections import defaultdict


class Solution(object):

    def dfs(self, origin):
        # print(origin)
        tmp = self.paths[origin]
        while tmp:
            via = tmp.pop()
            self.dfs(via)
        self.rtn.append(origin)

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        self.paths = defaultdict(list)
        for ticket in tickets:
            self.paths[ticket[0]].append(ticket[1])

        # print(self.paths)

        for key, val in self.paths.items():
            val.sort(reverse=True)

        self.rtn = []
        self.dfs('JFK')
        return (self.rtn[::-1])


sol = Solution()
tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
print(sol.findItinerary(tickets))
