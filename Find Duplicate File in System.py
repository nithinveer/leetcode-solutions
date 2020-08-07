class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        dct = {}
        for each_ in paths:
            spts = each_.split()
            dir = spts[0]
            for i in range(1, len(spts)):
                files = spts[i].split('(')
                if files[1] in dct :
                    tmp = dct[files[1]]
                    tmp.append(dir + '/' + files[0])
                    dct[files[1]] = tmp
                else:
                    tmp = []
                    tmp.append(dir + '/' + files[0])
                    dct[files[1]] = tmp
            # print(dct)
        rtn = []
        for each_key in dct.keys():
            if len(dct[each_key]) > 1:
                rtn.append(dct[each_key])
        return rtn



paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
sol = Solution()
print(sol.findDuplicate(paths))