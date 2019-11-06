def removeOuterParentheses( S):
    open = 0
    close = 0
    for i , j in enumerate(S[1:]):
        if j == '(':
            open+=1
        else:
            close +=1
        if close > open :
            S = S[1:i] + S[i+1:]
            break

    print(S)
    S = S[:-1]
    queue = []
    for i , j in enumerate(S):
        if j == '(':
            queue.append(i)
        else:
            queue.pop()
    print(queue)
    S = S[:queue[0]] + S[queue[0]+1:]
    print(S)


if __name__ == '__main__':
    S = "(()())(())(()(()))"
    print(removeOuterParentheses(S))
