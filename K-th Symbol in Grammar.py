def kthGrammar( N, K):

    def genGramm(N,K,Val):
        if N ==0:
            # print(Val[K-1])
            return (Val[K-1])
        temp = ''
        for each_char in Val:
            if len(temp) > K :
                break
            if each_char == '0':
                temp += '01'
            else:
                temp += '10'
        print(temp,N)

        return genGramm(N-1,K,temp)
    return (genGramm(N-1,K,'0'))


if __name__ == '__main__':
    N = 30
    K = 434991989
    print(kthGrammar(N,K))