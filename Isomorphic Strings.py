def isIsomorphic( s, t):
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









if __name__ == '__main__':
    s = "foo"
    t = "bar"
    print(isIsomorphic(s,t))