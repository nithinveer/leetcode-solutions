def wordBreak( s, wordDict):
    match_mapp = {}
    dp = [False for i in range(len(s) + 1)]
    dp[0] = True
    for i in range(1, len(s) + 1):
        for word in wordDict:
            if dp[i - len(word)] and s[i- len(word):i] == word:
                dp[i] = True
                # if (i - len(word)) not in match_mapp:


    print(dp)
    pos=[]
    for i in range(len(dp)):
        if dp[i] == True:
            pos.append(i - 1)
    pos.pop(0)
    res = []
    build(pos, s, "", res, wordDict, 0)
    return res


def build( pos, s, choice, res, wordDict, start):
    if start > pos[-1]:
        res.append(choice[:-1])
        return

    for i in range(len(pos)):
        if s[start: pos[i] + 1] in wordDict:
            build(pos, s, choice + s[start:pos[i] + 1] + " ", res, wordDict, pos[i] + 1)
    # return dp[-1]




if __name__ == '__main__':
    s = "catsanddogtonight"
    wordDict = ["cat", "cats", "and", "sand", "dog","to","night","tonight"]
    print(wordBreak(s,wordDict))