def nextGreaterElement( nums1, nums2):
    num_map = {}
    rtn_lst = []
    for i, j in enumerate(nums2):
        num_map[j] = i
    # print(num_map)
    for num in nums1:
        for j in range(num_map[num], len(nums2)):
            if nums2[j] > num:
                rtn_lst.append(nums2[j])
                break
            if j == len(nums2)-1:
                rtn_lst.append(-1)

    return(rtn_lst)

if __name__ == '__main__':
    nums1 = [2,4]
    nums2 = [1,2,3,4]
    print(nextGreaterElement(nums1,nums2))