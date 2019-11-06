def minSubArrayLen(s, nums):
    if len(nums) == 0:
        return 0

    temp =[nums[0]]
    sum = nums[0]
    min_len = 99999999
    if sum >=s :
        min_len =1

    for i in range(1,len(nums)):
        temp.append(nums[i])
        sum += nums[i]
        if sum >=s :
            while sum >=s :
                if min_len > len(temp):
                    min_len = len(temp)
                sum -=temp[0]
                del (temp[0])
    if min_len == 99999999:
        min_len = 0
    return  min_len



def rotate( nums, k):
    for i in range(k):
        temp = nums[-1]
        del(nums[-1])
        nums = [temp] + nums
    return(nums)

# def reverseWords(s):
#     temp = s.strip().split(" ")
#     print(temp)
#     temp.reverse()
#     for each
#     return(" ".join(temp))
#     return (" ".join(s.split(" ").reverse()))


def reverseWords(s):
    temp = ''
    for each_word in s.split(" "):
        temp = temp + " "+ (each_word[::-1])
    return temp.lstrip()

14
def movezeros(nums):
    max = len (nums)
    i =0
    dels = 0
    while i < max:
        if nums[i] ==0:
            del(nums[i])
            max -=1
            dels +=1
        else :
            i+=1
    for i in range(dels):
        nums.append(0)
    return(nums)

if __name__ == '__main__':
    s =  [0,1,0,3,12]
    # minSubArrayLen(s, nums)
    # print(rotate(nums,s))
    print(movezeros(s))