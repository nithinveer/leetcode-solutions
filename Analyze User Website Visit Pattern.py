from collections import defaultdict
class Solution(object):
    def pattern(self, lst):
        rt_set = set()
        if len(lst) < 3:
            return []
        for i in range(len(lst)-2):
            for j in range(i+1, len(lst)-1):
                for k in range(j+1, len(lst)):
                    rt_set.add(lst[i] + "#" + lst[j] + "#" + lst[k])
        return list(rt_set)
                    
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        tuples = [[i,j,k] for i, j , k in zip(username,timestamp,website)]
        tuples.sort(key = lambda  x:x[1])
        # print(tuples)

        users = defaultdict(list)
        for tup in tuples:
            users[tup[0]].append(tup[2])
        # print(users)
        mx = 0
        mx_val = []
        visits = defaultdict(int)
        for key in users.keys():
            for itr in self.pattern(users[key]):
                visits[itr]+=1
                if mx < visits[itr]:
                    mx = visits[itr]
                    mx_val = [itr]
                elif mx == visits[itr]:
                    mx_val.append(itr)
        mx_val.sort()
        # print( visits)
        return mx_val[0].split('#')
        





sol = Solution()






username = ["h","eiy","cq","h","cq","txldsscx","cq","txldsscx","h","cq","cq"]
timestamp = [527896567,334462937,517687281,134127993,859112386,159548699,51100299,444082139,926837079,317455832,411747930]
website = ["hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","yljmntrclw","hibympufi","yljmntrclw"]
print(sol.mostVisitedPattern(username,timestamp,website))