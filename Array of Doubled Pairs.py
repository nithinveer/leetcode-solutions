def canReorderDoubled( A):
    nums_mapp = {}
    for each_num in A:
        if each_num in nums_mapp:
            nums_mapp[each_num] += 1
        else:
            nums_mapp[each_num] = 1
    for each_num in sorted(A):
        if 2 * each_num in nums_mapp and each_num in nums_mapp:
            if nums_mapp[2 * each_num] == 1:
                nums_mapp.pop(2 * each_num)
            else:
                nums_mapp[2 * each_num] -= 1
            if each_num in nums_mapp and nums_mapp[each_num] == 1:
                nums_mapp.pop(each_num)
            elif each_num in nums_mapp:
                nums_mapp[each_num] -= 1
    if len(nums_mapp) == 0:
        return True
    else:
        return False





if __name__ == '__main__':
    A =  [1,2,4,16,8,4]
    print(canReorderDoubled(A))