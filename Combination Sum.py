def getPath(candidates, index, path, target,rtn_lst):
    print(path)
    if target < 0:
        return
    if target == 0:
        rtn_lst.append(path)
    for i in range(index, len(candidates)):
        getPath(candidates,i,path+ [candidates[i]],target-candidates[i],rtn_lst)
def combinationSum( candidates, target):
    rtn_lst = []
    # candidates.sort()
    getPath(candidates,0,[],target,rtn_lst)
    return rtn_lst
# Definition for a binary tree node.



if __name__ == '__main__':
    candidates = [2,3,6,7]
    target = 7
    print(combinationSum(candidates,target))