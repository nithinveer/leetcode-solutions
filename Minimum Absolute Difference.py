class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        diff_mapp = {}
        min_val = arr[-1]
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] not in diff_mapp:
                if (arr[i + 1] - arr[i]) < min_val:
                    min_val = arr[i + 1] - arr[i]
                temp = []
                temp.append([arr[i],arr[i+1]])
                diff_mapp[arr[i+1] - arr[i]] = temp
            else:
                if (arr[i + 1] - arr[i]) < min_val:
                    min_val = arr[i + 1] - arr[i]
                temp = diff_mapp[arr[i+1] - arr[i]]
                temp.append([arr[i], arr[i + 1]])
                diff_mapp[arr[i + 1] - arr[i]] = temp
        # min_val = arr[-1]
        # for k in list(diff_mapp.keys()):
        #     if k< min_val:
        #         min_val = k

        return diff_mapp[min_val]

arr = [3,8,-10,23,19,-4,-14,27]
sol = Solution()
print(sol.minimumAbsDifference(arr))