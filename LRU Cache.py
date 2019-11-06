class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.num_dict = {}
        self.lru = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.num_dict:
            if key not in self.lru:
                self.lru.append(key)
            self.lru = self.lru[-self.capacity:]
            print(self.num_dict, self.lru)
            return self.num_dict[key]
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if len(self.lru) == self.capacity:
            self.num_dict.pop(self.lru[0])
        if key not in self.num_dict:
            self.lru.append(key)

        self.num_dict[key] = value

        # self.lru.append(key)
        self.lru = self.lru[-self.capacity:]
        print(self.num_dict, self.lru)



obj = LRUCache(2)
print(obj.put(1,1))
print(obj.put(2,2))
print(obj.get(1))
print(obj.put(3,3))
# print(obj.put(4,1))
print(obj.get(2))
#
print(obj.put(4,4))
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))

