
def dailyTemperatures(T):
    rnt = [0] * len(T)
    stack = []
    print(rnt)
    for i, t in enumerate(T):
        print(i,t)
        while stack and t > stack[-1][1]:
            index, val = stack.pop()
            rnt[index] = i- index
        stack.append((i,t))
    return rnt

if __name__ == '__main__':
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    print(dailyTemperatures(T))