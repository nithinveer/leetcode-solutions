class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        move = 0
        for each_ in shift:
            if each_[0] == 0:
                move -= each_[1]
            else:
                move += each_[1]

        # print(move)
        if move > 0:
            move = move %len(s)
            if move>0:
                return s[-move:] + s[:len(s)-move]
            else:
                return s
        else:
            move = (-1*move)%len(s)
            # print(move)
            if move > 0:
                return s[move:]+s[:move]
            else:
                return s





sol = Solution()
s = "joiazl"
shift = [[1,1],[1,6],[0,1],[1,3],[1,0],[0,3]]
print(sol.stringShift(s,shift))