class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        lenght = len(cardPoints)
        totalSum = sum(cardPoints)
        subsum = 0
        for index in range(lenght-k):
            subsum += cardPoints[index]
        left = 1
        right = lenght -k
        answer = totalSum - subsum
        while right < lenght :
            subsum +=  cardPoints[right]
            subsum -= cardPoints[left-1]
            answer = max(answer, totalSum - subsum)
            right +=1
            left +=1
            
        return answer