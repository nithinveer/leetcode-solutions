class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        rtn = []
        splits = path.split('/')
        for each_ in splits:
            if each_ == '..':
                if len(rtn)> 0:
                    rtn.pop()
            elif not each_ or each_ == '.':
                continue
            else:
                rtn.append(each_)
        return("/"+"/".join(e for e in rtn))



sol = Solution()
path = "/a//b////c/d//././/.."
print(sol.simplifyPath(path))