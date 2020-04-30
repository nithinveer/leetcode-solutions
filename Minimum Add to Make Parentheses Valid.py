class Solution(object):
    # def minAddToMakeValid(self, S):
    #     """
    #     :type S: str
    #     :rtype: int
    #     """
    #     stack = []
    #     close_cnt =0
    #     for each_ in S:
    #         if each_ == '(':
    #             stack.append('(')
    #         else:
    #             if len(stack) > 0:
    #                 stack.pop()
    #             else:
    #                 close_cnt+=1
    #     return(len(stack)+close_cnt)

    def minAddToMakeValid(self, S):
        open_cnt = 0
        close_cnt = 0
        for each_ in S:
            if each_ == '(':
                open_cnt+=1
            else:
                if open_cnt >0:
                    open_cnt-=1
                else:
                    close_cnt+=1
        print(open_cnt+close_cnt)




sol = Solution()
S= "()))(("
sol.minAddToMakeValid(S)