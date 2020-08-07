from collections import deque
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        visited = [False for i in range(len(graph))]
        A = set()
        B = set()
        A.add(0)
        visited[0] = True
        for each_ in graph[0]:
            B.add(each_)
            visited[each_] = True
            for _each in graph[each_]:
                if _each in B:
                    return False
                else:
                    A.add(_each)
                    visited[_each] = True
        # print(A)
        # print(B)
        # print(visited)
        que = deque([i for i in range(1,len(graph))])
        while len(que) >0:
            tmp = que.popleft()

            if tmp in A or tmp in B:

                if tmp in A:
                    for each_ in graph[tmp]:
                        if each_ in A:
                            return False
                        else:
                            B.add(each_)
                            # visited[each_] = True
                if tmp in B:
                    for each_ in graph[tmp]:
                        if each_ in B:
                            return False
                        else:
                            A.add(each_)

            else:
                if len(graph[tmp]) == 0:
                    A.add(tmp)
                if visited[tmp]:
                    A.add(tmp)
                    for each_ in graph[tmp]:
                        B.add(each_)
                # else:
                que.append(tmp)

            visited[tmp] = True
            # print(que,A,B)
        return True

sol = Solution()

graph = [[1],[0],[4],[4],[2,3]]
print(sol.isBipartite(graph))