class StockSpanner:

    def __init__(self):
        self.stack=[]

    def next(self, price: int) -> int:
        count=1
        tmp=[]
        while self.stack:
            prev=self.stack.pop()
            tmp.append(prev)
            if price>=prev:
                count+=1
            else:
                break
        self.stack.extend(tmp[::-1])
        self.stack.append(price)
        return count

            


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)