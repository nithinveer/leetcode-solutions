class Solution(object):
    def area(self, heights):
        stack = [-1]

        maxarea = 0
        for i in range(len(heights)):

            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                maxarea = max(maxarea, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)

        while stack[-1] != -1:
            maxarea = max(maxarea, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return maxarea
                
    
    
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or len(matrix) == 0:
            return 0
        hist = [0]* len(matrix[0])
        for i in range(len(matrix[0])):
            hist[i] = int(matrix[0][i])
        area = self.area(hist)
        # print(area)
        for i in range(1, len(matrix)):
            for j in range(len(hist)):
                if int(matrix[i][j]) == 0:
                    hist[j] = 0
                else:
                    hist[j] += int(matrix[i][j])
            area = max(area, self.area(hist))
            # print(hist, area)
        return area


sol = Solution()
matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
print(sol.maximalRectangle(matrix))