from collections import  defaultdict
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        dct = defaultdict(list)
        for each in edges:
            dct[each[0]].append(each[1])
            dct[each[1]].append(each[0])
        count = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                count +=1
                tmp = [i]
                visited.add(i)
                while(len(tmp)) > 0:
                    tmp_ = []
                    for each_ in tmp:
                        for itr in dct[each_]:
                            if itr not in visited:
                                visited.add(itr)
                                tmp_.append(itr)
                    tmp = tmp_
                        
            
        return(count)


sol = Solution()
n = 5
edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
sol.countComponents(n, edges)