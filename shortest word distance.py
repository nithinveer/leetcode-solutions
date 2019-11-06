def shortestDistance( words, word1, word2):
    if word1 != word2:
        word1_found = False
        word2_found = False
        rtn_val = len(words)
        for i in range(0, len(words)):
            if words[i] == word1:
                p1 = i
                word1_found = True
            elif  words[i] == word2:
                p2 = i
                word2_found = True
            # print(p1, p2, word1_found, word2_found)
            if word1_found and word2_found and (abs(p1-p2) < rtn_val):
                    rtn_val = abs(p1-p2)

        return (rtn_val)
    else:
        # print(True)
        p = len(words)
        rtn_val = len(words)
        for i in range(0, len(words)):
            if words[i] == word1:
                # print(p, i)
                if abs(p-i) < rtn_val:
                    rtn_val = abs(p-i)
                p = i

        return rtn_val



    # p1 = words.index(word1)
    # p2 = words.index(word2)
    # if (words.index(word1) - words.index(word2)) > 0:
    #     return (words.index(word1) - words.index(word2))
    # else :
    #     return (words.index(word1) - words.index(word2))*-1

if __name__ == '__main__':
    words = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "makes"
    word2 = "makes"
    print(shortestDistance(words, word1, word2))