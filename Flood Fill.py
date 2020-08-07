class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        org = image[sr][sc]
        image[sr][sc] = newColor
        if org == newColor:
            return image
        rows = len(image)
        cols = len(image[0])

        def scan(row,col):
            if row-1 >=0 and image[row-1][col] == org:
                image[row-1][col] = newColor
                scan(row-1,col)
            if  row+1 < rows and image[row+1][col] == org:
                image[row+1][col] = newColor
                scan(row+1,col)
            if col-1 >=0 and image[row][col-1] == org:
                image[row][col-1] = newColor
                scan(row,col-1)
            if  col+1 < cols and image[row][col+1] == org:
                image[row][col+1] = newColor
                scan(row,col+1)

        scan(sr,sc)
        return image



image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
sol = Solution()
print(sol.floodFill(image,sr,sc,newColor))