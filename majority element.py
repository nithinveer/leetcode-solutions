def majorityElement( nums):
    dump = {}
    for each_num in nums:
        if each_num in dump:
            dump[each_num] +=1
        else:
            dump[each_num] = 1
    for each_key in list(dump.keys()):
        if dump[each_key] > int(len(nums)/2):
            return each_key

if __name__ == '__main__':
    nums = [3,2,3]
    print(majorityElement(nums))