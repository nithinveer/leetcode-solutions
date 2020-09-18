from collections import deque


class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        last = len(graph) - 1
        queue = deque([[0, [0]]])
        rtn = []
        while queue:
            [node, vis] = queue.popleft()
            for each in graph[node]:
                viscopy = vis[:]
                if each == last:
                    viscopy.append(each)
                    rtn.append(viscopy)
                else:
                    viscopy.append(each)
                    queue.append([each, viscopy])
        return rtn


sol = Solution()
graph = [[1, 2], [3], [3], []]
print(sol.allPathsSourceTarget(graph))
