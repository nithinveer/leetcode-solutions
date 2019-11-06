import collections
def spiral():
    input =     [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9  ],
        [10,11,12]
    ]


    cm = 0
    cM = len(input[0])-1
    rm = 0
    rM = len(input)-1
    result = []
    a= True
    b= False
    c= False
    d= False
    while True:
        if len(result) == len(input)*len(input[0]):
            break
        if a and (rm<=rM and cm<=cM):
            for i in range(cm, cM+1):
                result.append(input[rm][i])
            rm +=1
            a = False
            b = True
            print(rm, rM, cm, cM)
        if b and (rm<=rM and cm<=cM):
            # print(rm,rM, cm, cM)
            for i in range(rm,rM+1):
                result.append(input[i][cM])
            cM -= 1
            b=False
            c= True
        if c and (rm<=rM and cm<=cM):
            # print(rm, rM, cm, cM)
            for i in range(cM,cm-1,-1):
                # print(rM,i)
                result.append(input[rM][i])
            rM -=1
            c= False
            d = True
        if d and (rm<=rM and cm<=cM):
            # print(rm, rM, cm, cM)
            for i in range(rM, rm-1,-1):
                result.append(input[i][cm])
            cm +=1
            d= False
            a = True
        # print(rm, rM, cm, cM)
        # time.sleep(5)
    print(result)

def insert_spiral(n):
    # temp = []
    # for i in range(n):
    #     temp.append(0)
    # input = []
    # for i in range(n):
    #     input.append(temp)
    input = [[0 for _ in range(n)] for _ in range(n)]
    print(input)
    # input = collections.defaultdict(list)
    cm = 0
    cM = n - 1
    rm = 0
    rM = n - 1
    result = []
    print(rm, rM, cm, cM)
    a = True
    b = False
    c = False
    d = False
    start = 1
    while True:
        if len(result) == len(input) * len(input[0]):
            break
        if a and (rm <= rM and cm <= cM):
            for i in range(cm, cM + 1):
                print(start, rm, i,input[rm][i])
                input[rm][i] = start
                start+=1
                result.append(input[rm][i])

            rm += 1
            a = False
            b = True
        print(input)
        print(result)
            # exit(0)
            # print(rm, rM, cm, cM)
        if b and (rm <= rM and cm <= cM):
            # print(rm,rM, cm, cM)
            for i in range(rm, rM + 1):
                print(start, i , cM, input[i][cM])
                input[i][cM] = start
                start+=1
                result.append(input[i][cM])
                print(input)
            cM -= 1
            b = False
            c = True
        if c and (rm <= rM and cm <= cM):
            # print(rm, rM, cm, cM)
            for i in range(cM, cm - 1, -1):
                print(start, rM, i)
                # print(rM,i)
                input[rM][i] = start
                start+=1
                result.append(input[rM][i])
            rM -= 1
            c = False
            d = True
        if d and (rm <= rM and cm <= cM):
            # print(rm, rM, cm, cM)
            for i in range(rM, rm - 1, -1):
                print(start, i , cm)
                input[i][cm] = start
                start+=1
                result.append(input[i][cm])
            cm += 1
            d = False
            a = True



    print(input)
    # print(result)

def preorderTraversal( root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root is None:
        return []
    stack = [root]
    output = []
    while stack:
        root = stack.pop()
        if root is not None:
            output.append(root.val)
        if root.right is not None:
            stack.append(root.right)
        if root.left is not None:
            stack.append(root.left)

    return output

if __name__ == '__main__':
    arr = [1,null,2,3]
