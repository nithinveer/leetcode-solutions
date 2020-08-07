class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        rtn = 0
        rtn_lst = []
        prev= ''
        count = 0
        for each_ in chars:
            chars = chars[1:]
            if each_ == prev:
                count +=1
            else:
                if count >=  2:
                    rtn += (len(str(count)) +1)
                    rtn_lst.append(prev)
                    for _each in str(count):
                        rtn_lst.append(_each)
                elif count == 1:
                    rtn +=1
                    rtn_lst.append(prev)
                # else:
                prev = each_
                count =1
        if count >=2 :
            rtn += (len(str(count)) + 1)
            rtn_lst.append(prev)
            for _each in str(count):
                rtn_lst.append(_each)
        elif count ==1:
            rtn +=1
            rtn_lst.append(prev)
        chars = rtn_lst
        return(rtn)



chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
sol = Solution()
print(sol.compress(chars))