from collections import defaultdict
class Solution(object):
    def mostVisited(self, n, rounds):
        """
        :type n: int
        :type rounds: List[int]
        :rtype: List[int]
        """
        dct = defaultdict(int)
        mx = []
        max_val = 0
        for i in range(1, len(rounds)):
            if rounds[i-1] < rounds[i]:
                for j in range(rounds[i-1], rounds[i]):
                    dct[j] +=1
                    if dct[j] > max_val:
                        max_val = dct[j]
                        mx = [j]
                    elif dct[j] == max_val:
                        mx.append(j)
            else:
                for j in range(rounds[i - 1], n+rounds[i] ):
                    if j > n:
                        j = j-n
                    dct[j] += 1
                    if dct[j] > max_val:
                        max_val = dct[j]
                        mx = [j]
                    elif dct[j] == max_val:
                        mx.append(j)
            # print(dct)
        dct[rounds[-1]] += 1
        if dct[rounds[-1]] > max_val:
            max_val = dct[rounds[-1]]
            mx = [rounds[-1]]
        elif dct[rounds[-1]] == max_val:
            mx.append(rounds[-1])
        mx.sort()
        return(mx)

        
        






sol = Solution()
n = 2
rounds = [2,1,2,1,2,1,2,1,2]
print(sol.mostVisited(n, rounds))