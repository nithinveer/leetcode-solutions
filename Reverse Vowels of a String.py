def reverseVowels( s):
    i =0
    vo = ['a','e','i','o','u','A','E','I','O','U']
    j = len(s) -1
    while i <j:


        if s[i] in vo and s[j] in vo :
            print(i,j)

            s = s[0:i] + s[j] + s[i+1:j] +s [i] + s[j+1:]
            i+=1
            j -=1
            print(s)
        else :
            if s[i] not in vo:
                i += 1
            if s[j] not in vo:
                j -= 1

    return  s








if __name__ == '__main__':
    s = "aA"
    print(reverseVowels(s))