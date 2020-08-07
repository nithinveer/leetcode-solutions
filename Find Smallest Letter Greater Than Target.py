class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if ord(letters[-1]) <= ord(target) or ord(target) < ord(letters[0]):
            return letters[0]
        left = 0
        right = len(letters) -1

        while left < right:
            mid = (left + right) //2
            if ord(letters[mid]) <= ord(target) :
                left = mid+1
            # elif ord(letters[mid]) > ord(target) :


            else:
                right = mid


        # print(letters[left], letters[right])
        if ord(letters[left]) > ord(target):
            return letters[left]
        else:
            return letters[right]

sol = Solution()
letters = ["c","d" ,"f", "j"]
target = "c"
print(sol.nextGreatestLetter(letters,target))