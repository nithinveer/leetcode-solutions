class ProductOfNumbers(object):

    def __init__(self):
        self.nums = []
        self.zero = -1

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.nums.append(1)
            self.zero = len(self.nums) -1
        elif len(self.nums) == 0:
            self.nums.append(num)
        else:
            last = self.nums[-1]
            if last == 0:
                self.nums.append(num)
            else:
                self.nums.append(num* last)
        # print(self.nums)

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        n = len(self.nums)
        if self.zero > n-1-k:
            return 0
        else:
            num = self.nums[-1]
            if  n-1-k < 0:
                deno  = 1
            else:
                deno = self.nums[max(0, n-1-k)]
            return int(num/deno)


# ["ProductOfNumbers","add","getProduct","getProduct","add","add","getProduct","add","getProduct","add","getProduct","add","getProduct"
#     ,"getProduct","add","getProduct"]
# [[],[7],[1],[1],[4],[5],[3],[4],[4],[3],[4],[8],[1],[6],[2],[3]]

productOfNumbers =  ProductOfNumbers()
print(productOfNumbers.add(7))
print(productOfNumbers.getProduct(1))
print(productOfNumbers.getProduct(1))
print(productOfNumbers.add(4))
print(productOfNumbers.add(5))
print(productOfNumbers.getProduct(3))
print(productOfNumbers.add(4))
print(productOfNumbers.getProduct(4))
print(productOfNumbers.add(3))
print(productOfNumbers.getProduct(4))
print(productOfNumbers.add(8))
print(productOfNumbers.getProduct(1))
print(productOfNumbers.getProduct(6))
print(productOfNumbers.add(2))
print(productOfNumbers.getProduct(3))



# print(productOfNumbers.getProduct(4))
# print(productOfNumbers.add(8))
# print(productOfNumbers.getProduct(2))