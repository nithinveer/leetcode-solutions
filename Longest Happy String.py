import heapq
class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        tmp =[]
        if a >0:
            tmp.append((-a,'a'))
        if b > 0:
            tmp.append((-b,'b'))
        if c > 0:
            tmp.append((-c, 'c'))
        heapq.heapify(tmp)
        can = True
        rtn = ''
        cnt = 0
        prev = ''
        while can and tmp:
            num, char = heapq.heappop(tmp)
            if char == prev and cnt == 2:
                if tmp:
                    num2, char2 = heapq.heappop(tmp)
                    rtn+= char2
                    if num2 < -1:
                        heapq.heappush(tmp,(num2+1,char2))
                    heapq.heappush(tmp,(num, char))
                    cnt = 1
                    prev = char2
                else:
                    break
            else:
                rtn+= char
                if num <- 1:
                    heapq.heappush(tmp, (num + 1, char))
                if prev == char:
                    cnt +=1
                else:
                    cnt = 1
                    prev = char

        return rtn


sol = Solution()
a = 1
b = 1
c = 7
print(sol.longestDiverseString(a,b,c))