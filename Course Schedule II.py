class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        rtn_lst = []
        if len(prerequisites) == 0:
            for i in range(numCourses):
                rtn_lst.append(i)
            return rtn_lst
        dict = {}
        course = {}
        pass_set = set()
        for i in range(numCourses):
            dict[i] = 0
            course[i] = []
            pass_set.add(i)
        for each_ in prerequisites:
            dict[each_[0]] +=1
            tmp = course[each_[1]]
            tmp.append(each_[0])
            course[each_[1]] = tmp
            if each_[0] in pass_set:
                pass_set.remove(each_[0])
        while len(pass_set) >0:
            tmp_set =set()
            for each_ in list(pass_set):
                rtn_lst.append(each_)
                dict.pop(each_)
                for _each in course[each_]:
                    dict[_each] -=1
                    if dict[_each] == 0:
                        tmp_set.add(_each)
            # print(dict,pass_set,course,tmp_set)
            pass_set = tmp_set
        if len(dict) > 0:
            return  []

        # print(dict,pass_set,course)
        return rtn_lst




sol = Solution()
numCourses = 9
# prerequisites = [[1,0]]
prerequisites = [[2,5],[3,5],[1,3],[1,2],[0,1],[4,2],[7,6],[8,6]]
print(sol.findOrder(numCourses,prerequisites))