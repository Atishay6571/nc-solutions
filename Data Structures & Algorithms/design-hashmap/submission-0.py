class MyHashMap:

    def __init__(self):
        self.hmap=[]

    def put(self, key: int, value: int) -> None:
        for i in self.hmap:
            if key==i[0]:
                i[1]=value
                break
        else:
            self.hmap.append([key,value])

    def get(self, key: int) -> int:
        for i in self.hmap:
            if i[0]==key:
                return i[1]
        else:
            return -1

    def remove(self, key: int) -> None:
        for i in self.hmap:
            if i[0]==key:
                self.hmap.remove(i)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)