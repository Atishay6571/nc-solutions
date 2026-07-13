class FreqStack:
    from collections import defaultdict
    def __init__(self):
        self.hmap=defaultdict(int)
        self.stack=[]
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.hmap[val]+=1

    def pop(self) -> int:
        tmp=[]
        #max value logic here
        maximum=max(self.hmap.values())
        maxkeys =[]
        for k,v in self.hmap.items():
            if maximum==v:
                maxkeys.append(k)

        while self.stack:
            element= self.stack.pop()
            if element in maxkeys:
                self.hmap[element]-=1
                break
            tmp.append(element)
        while tmp:
            self.stack.append(tmp.pop(0))

        return element


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()