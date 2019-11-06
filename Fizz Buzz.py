def fizzBuzz( n):
    rtn_lst = []
    for i in range(1, n+1):
        if i%15 == 0:
            rtn_lst.append("FizzBuzz")
        elif i%3 ==0:
            rtn_lst.append("Fizz")
        elif i%5 ==0:
            rtn_lst.append("Buzz")
        else:
            rtn_lst.append(str(i))
    return rtn_lst


if __name__ == '__main__':
    n = 19
    print(fizzBuzz(n))