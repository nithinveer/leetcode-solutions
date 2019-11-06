def removeDuplicates( S):
    stack = []
    for each_char in S:
        if len(stack) > 0 and stack[-1] == each_char:
            stack.pop()
        else:
            stack.append(each_char)


    return ''.join(x for x in stack)









if __name__ == '__main__':
    S =  "abbaca"
    print(removeDuplicates(S))