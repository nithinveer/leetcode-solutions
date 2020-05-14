class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        dict = {}
        for each_ in items:
            if each_[0] in dict:
                tmp = dict[each_[0]]
                # print(len(tmp))
                if len(tmp) >= 5:
                    mn  = min(tmp)
                    if each_[1] > mn:
                        tmp.remove(mn)
                        tmp.append(each_[1])
                else:
                    tmp.append(each_[1])
                dict[each_[0]] = tmp
            else:
                tmp = []
                tmp.append(each_[1])
                dict[each_[0]] = tmp
        # print(dict)
        for each_ in dict.keys():
            dict[each_] = sum(dict[each_])//5
        # print(dict)
        rtn = []
        for i in range(1,1001):
            if i in dict:
                rtn.append([i,dict[i]])
        return rtn



items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76],[1,41]]

sol = Solution()
print(sol.highFive(items))