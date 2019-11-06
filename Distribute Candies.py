def distributeCandies( candies):
    rtn_mapp = []
    for each_can in candies:
        if each_can not in rtn_mapp:
            rtn_mapp.append(each_can)

    # print(len(rtn_mapp))
    if len(rtn_mapp) < (len(candies))/2 :
        return len(rtn_mapp)
    else:
        return  int((len(candies)/2))









if __name__ == '__main__':
    candies = [1,1,2,3]
    # print(distributeCandies(candies))
    i = 2
    p = 2 * i + 1
    print(p)