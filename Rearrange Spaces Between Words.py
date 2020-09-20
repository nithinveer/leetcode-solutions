class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        originalLength = len(text)
        words = text.split()
        text = text.replace(" ","")
        newLength = len(text)
        spaces = originalLength - newLength
        if len(words) == 1:
            end = ''
            while spaces > 0:
                end +=' '
                spaces -=1
            return  words[0] + end
        wordSpace = spaces//(len(words)-1)
        endSpace = spaces%(len(words) -1 )
        separator = ''
        while wordSpace >0:
            separator += ' '
            wordSpace -=1
        esndseparsator = ''
        while endSpace > 0:
            esndseparsator += ' '
            endSpace-=1
        return separator.join(words) + esndseparsator





sol = Solution()
text =  "a"
print(sol.reorderSpaces(text))