class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        first = len(S) -1
        sec = len(T) -1
        first_count = 0
        sec_count = 0
        while first >= 0 or sec >= 0:
            while first >=0:
                print(first,first_count)
                if S[first] == '#':
                    first_count +=1
                    first -=1
                elif S[first] != '#' and first_count >0:
                    first -=1
                    first_count -=1
                else :
                    break
            while sec >=0:
                print(sec,sec_count)
                if T[sec] == '#':
                    sec_count +=1
                    sec -=1
                elif T[sec] != '#' and sec_count >0:
                    sec -=1
                    sec_count -=1
                else :
                    break

            print("las", first,S[first],sec,T[sec],first_count,sec_count)

            if first <0 and sec <0:
                return True
            if first >=0 and sec < 0 :
                return False
            if sec >=0 and first <0:
                return False
            if first >= 0 and sec >= 0 and  (S[first] != T[sec]) :
                return False
            first -=1
            sec -=1
            # if first >=0 and sec < 0 :
            #     return False
            # if sec >=0 and first <0:
            #     return False
        return True





        #     print(first,sec)
        #     t_first = first
        #     t_sec = sec
        #     first_count = 0
        #     sec_count = 0
        #     while S[t_first] == '#':
        #         first_count +=1
        #         t_first -=1
        #     while T[t_sec] == '#':
        #         sec_count+=1
        #         t_sec -=1
        #
        #     print("mIS",first, sec,first_count,sec_count)
        #     first = first - 2*first_count
        #     sec = sec - 2*sec_count
        #     print(S[first] ,T[sec])
        #     if S[first] != T[sec] :
        #         return False
        #     first -=1
        #     sec -=1
        #
        # return True







sol = Solution()
S= "bbbextm"
T = "bbb#extm"
print(sol.backspaceCompare(S,T))