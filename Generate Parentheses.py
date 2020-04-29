class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rtn_lst = []
        left=n
        right = n
        adder = ['(',')']

        def builder(left,right, curr_str) :

            if left <= 0 and right <= 0 and curr_str not in rtn_lst :
                rtn_lst.append(curr_str)
            else:
                for i in range(2):
                    # print(left, right, curr_str)
                    if adder[i] == '(' and left >0:
                        new_str = curr_str + '('
                        builder(left-1,right,new_str)
                    elif adder[i] == ')' and right > left:
                        new_str = curr_str + ')'
                        builder(left,right-1,new_str)

        curr_str = ''
        builder(n,n,curr_str)
        return(rtn_lst)
sol = Solution()

n =2
print(sol.generateParenthesis(n))
