def sortArrayByParity( A):
    odd_list = []
    even_list = []
    for each_ele in A:
        if each_ele%2 == 0:
            even_list.append(each_ele)
        else:
            odd_list.append(each_ele)
    return even_list + odd_list    







if __name__ == '__main__':
    A  = [3,1,2,4]
    print(sortArrayByParity(A))