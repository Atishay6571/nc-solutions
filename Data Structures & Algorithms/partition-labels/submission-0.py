class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hmap=defaultdict(int)
        for element in s:
            hmap[element]+=1
        #traverse through each character and decide whether
        #new partition can be created
        # need to maintain the current elements of partition
        queue=[]
        partition=0
        result=[]
        for i in range(len(s)):
            partition+=1
            hmap[s[i]]-=1
            if s[i] not in queue:
                queue.append(s[i])
            if hmap[s[i]]==0:
                queue.remove(s[i])
                if not queue:
                    result.append(partition)
                    partition=0
        return result