class Solution(object):
    def expand(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        itr_slt = []
        tmp = []
        isClosed = True
        tmp_str = ''
        for i in range(len(s)):
            # print(itr_slt,s[i], isClosed,tmp_str)
            if s[i] == '{':
                if len(tmp_str) > 0:
                    p_tmp = []
                    p_tmp.append(tmp_str)
                    itr_slt.append(p_tmp)
                tmp_str = ''
                isClosed = False
            elif s[i] == '}':
                tmp.sort()
                itr_slt.append(tmp)
                tmp = []
                isClosed = True
            elif s[i] == ',':
                continue
            else :
                if isClosed:
                    tmp_str +=s[i]
                else:
                    tmp.append(s[i])
        if len(tmp) > 0:
            tmp.sort()
            itr_slt.append(tmp)
        if len(tmp_str) > 0:
            p_tmp= []
            p_tmp.append(tmp_str)
            itr_slt.append(p_tmp)

        print(itr_slt)

        rtn_lst = []
        def addtn(curr_str,itr):
            if itr >= len(itr_slt):
                rtn_lst.append(curr_str)
            else:
                for each_ in itr_slt[itr]:
                    tmp_str = curr_str + each_
                    addtn(tmp_str,itr+1)
        
        addtn('',0)
        return(rtn_lst)




sol = Solution()
s = "{a,b}{z,x,y}"
print(sol.expand(s))