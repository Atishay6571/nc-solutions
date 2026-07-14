class TimeMap:
    from collections import defaultdict
    def __init__(self):
        self.store=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res=-1
        val=self.store[key]
        l,r= 0,len(val)-1
        while l<=r:
            mid=(l+r)//2
            if val[mid][1]>timestamp:
                r=mid-1
            elif val[mid][1]<timestamp:
                l=mid+1
                res=mid
            else:
                res=mid
                break
        if res==-1:
            return ""
        else:
            return val[res][0]
            
