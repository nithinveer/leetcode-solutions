from _collections import  defaultdict
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n - 1: return False
        dct = defaultdict(list)
        for edge in edges:
            dct[edge[0]].append(edge[1])
            dct[edge[1]].append(edge[0])
        previous  = set()
        visited = set()
        count = 0
        for i in range(n):

            if i not in visited:
                if count > 1:
                    return False
                tmp = [(i,-1)]
                while(len(tmp)) > 0:
                    tmp_ = []
                    for each in tmp:
                        for itr in dct[each[0]]:
                            if itr == each[1]:
                                continue
                            else:
                                if itr in visited:
                                    print(each, dct[each[0]], visited)
                                    return  False
                                tmp_.append((itr, each[0]))
                        visited.add(each[0])
                    tmp = tmp_
            count +=1
        return True





sol = Solution()
n = 5
edges =[[0,1],[0,2],[0,3],[1,4]]
print(sol.validTree(n, edges))