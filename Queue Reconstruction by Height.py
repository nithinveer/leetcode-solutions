class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        keyss = {}
        for  each in people:
            if each[0] not in keyss:
                tmp = []
                tmp.append(each[1])
                keyss[each[0]] = tmp
            else:
                tmp = keyss[each[0]]
                tmp.append(each[1])
                keyss[each[0]] = tmp


        for each_ in keyss.keys():
            tmp = keyss[each_]
            tmp.sort()
            keyss[each_] = tmp
        # print(keyss)
        tmp = list(keyss.keys())
        tmp.sort(reverse=True)
        # print(tmp)
        rtn = []
        for each_ in tmp:
            for _each in keyss[each_]:
                rtn.insert(_each,[each_,_each])
        return(rtn)


people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
sol = Solution()
print(sol.reconstructQueue(people))