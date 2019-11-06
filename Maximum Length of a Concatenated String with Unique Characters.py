def maxLength( arr):
    if len(arr) ==1:
        return len(arr[0])
    arr2 = sorted(arr, key=len)
    print(arr2)
    set_list = []





if __name__ == '__main__':
    arr = ["cha", "r", "act", "ers"]
    print(maxLength(arr))
