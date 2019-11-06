class PriorityQueue(object):
    def __init__(self):
        self.queue = []
        self.map_nums = {}

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

        # for checking if the queue is empty

    def isEmpty(self):
        return len(self.queue) == []

    def createMap(self):
        num_map = {}
        for each_num in self.queue:
            if each_num in num_map:
                num_map[each_num] +=1
            else :
                num_map[each_num] = 1
        return num_map

        # for inserting an element in the queue

    def push(self, x):
        self.queue.append(x)
        if x in self.map_nums:
            self.map_nums[x] += 1
        else:
            self.map_nums[x] = 1

        # for popping an element based on Priority

    def pop(self):
        # try:
        # queue_map = self.createMap()
        # print(queue_map,self.queue)
        # exit(0)
        max =0
        for i in range(len(self.queue)):
            # print(self.queue[i], self.queue[max])
            if self.map_nums[self.queue[i]] >= self.map_nums[self.queue[max]]:
                max = i

        item = self.queue[max]
        # print(i, item)
        # exit(0)
        print(self.map_nums)
        print(max, self.queue,self.queue[max])
        if self.map_nums[self.queue[max]] == 1:
            self.map_nums.pop(self.queue[max])
        else:
            self.map_nums[self.queue[max]] -=1
        del self.queue[max]
        return item
        # except Exception as ex:
        #     print(str(ex))
        #     exit()


if __name__ == '__main__':
    myQueue = PriorityQueue()
    myQueue.push(12)
    myQueue.push(14)
    myQueue.push(1)
    myQueue.push(12)
    myQueue.push(14)
    myQueue.push(7)
    myQueue.push(14)
    myQueue.push(7)
    print(myQueue)
    myQueue.pop()
    print(myQueue)
    myQueue.pop()
    print(myQueue)
    myQueue.pop()
    print(myQueue)
    myQueue.pop()
    print(myQueue)
    # while not myQueue.isEmpty():
    #     print(myQueue)
    #     print(myQueue.pop())
