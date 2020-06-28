class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        in_dict = {}
        out_dict = {}
        for each_ in connections:
            if each_[0] in in_dict:
                tmp = in_dict[each_[0]]
                tmp.append(each_[1])
                in_dict[each_[0]] = tmp
            else:
                tmp = []
                tmp.append(each_[1])
                in_dict[each_[0]] = tmp

            if each_[1] in out_dict:
                tmp = out_dict[each_[1]]
                tmp.append(each_[0])
                out_dict[each_[1]] = tmp
            else:
                tmp = []
                tmp.append(each_[0])
                out_dict[each_[1]] = tmp

        # print(in_dict, out_dict)

        itr = [0]
        count =  0
        visited = set()
        while len(itr) > 0:
            tmp = set()
            for each_ in itr:
                if each_ in out_dict:
                    for _each in out_dict[each_] :
                        if _each not in visited:
                            tmp.add(_each)


                if each_ in in_dict:
                    for _each in in_dict[each_]:
                        if _each not in visited:
                            tmp.add(_each)
                            count +=1
                visited.add(each_)
            # print(tmp,itr,count)
            itr = list(tmp)

        return count

n = 6
connections = [[1,0],[2,0]]
sol = Solution()
print(sol.minReorder(n,connections))