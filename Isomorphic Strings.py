def isIsomorphicold( s, t):
    dup = {}
    for i  in range(0,len(s)):
        if s[i] in dup :
            if dup[s[i]] != t[i]:
                return False
        else :
            if t[i] in list(dup.values()):
                return False
            dup[s[i]] = t[i]
    return True




def isIsomorphic( s, t):
    dup = {}
    dup_rev = {}
    for i in range(len(s)):
        if s[i] not in dup_rev:
            if t[i] in dup:
                return False
            else:
                dup[t[i]]  = s[i]
                dup_rev[s[i]] = t[i]

        else:
            if dup_rev[s[i]] != t[i]:
                return False

        #     dup_rev[s[i]] = t[i]
        #
        # if t[i] in dup:
        #     if dup[t[i]] != s[i]:
        #         return False
        #
        # else:
        #     dup[t[i]] = s[i]
    return True




if __name__ == '__main__':
    s = "paper"
    t = "title"
    print(isIsomorphic(s,t))