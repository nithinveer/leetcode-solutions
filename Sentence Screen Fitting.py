class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        lgt = len(sentence)
        dct = {}
        idx = 0
        for row in range(rows):
            start = idx % lgt
            if start in dct:
                idx += dct[start]
            else:
                cnt, col, piv = 0, 0, start
                while col + len(sentence[piv]) <= cols:
                    col += len(sentence[piv]) + 1
                    piv = (piv + 1) % lgt
                    cnt += 1
                dct[start] = cnt
                idx += cnt
        return (idx//lgt)
    
    def wordsTypingBruteForce(self, sentence, rows, cols):   
        # Brute force method iterates over each word and 
        # counts the times of fit until all rows have been consumed
        # This leads to TLE
        # Lets modify it by identifing the patterns and
        # Store the patterns in a dictionay. - Now refer to the wordsTypingBrute function
        idx = row = col = 0
        while row < rows :
            # print(idx%lgt, row, col)
            if col + len(sentence[idx%lgt]) <= cols:
                col += len(sentence[idx%lgt]) +1
                idx += 1
                if col > cols:
                    col = 0
                    row+=1
            else:
                row +=1
                col = 0
            
        return (idx//lgt)