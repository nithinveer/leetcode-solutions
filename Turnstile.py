from collections import deque
def turnstile(numCustomers, arrTime, direction):
    inque = deque([])
    outque = deque([])
    piv = 0
    rtn = [-1]* numCustomers
    isOut = False
    # print(rtn)
    while arrTime[piv] == 0:
        if direction[piv] == 1:
            outque.append(piv)
            isOut = True
        else:
            inque.append(piv)
        piv+=1
    cost = 0
    while inque or outque or piv < numCustomers:
        print(inque, outque, piv, isOut)
        while piv < numCustomers and arrTime[piv] == cost:
            if direction[piv] == 1:
                outque.append(piv)
            else:
                inque.append(piv)
            piv += 1
        if (isOut and outque )or (not inque and not isOut and outque):
            popindex = outque.popleft()
            rtn[popindex] = cost
            cost+=1
            isOut = True
        elif inque:
            popindex = inque.popleft()
            rtn[popindex] = cost
            cost+=1
            isOut = False
        else:
            isOut = True
            cost+=1
        print(rtn)
    return rtn


    
    
    
numCustomers = 4
arrTime =   [0,0,1,5]
direction = [0,1,1,0]
print(turnstile(numCustomers, arrTime,direction))