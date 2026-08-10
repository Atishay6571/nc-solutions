class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # prefix sum
        running = 0
        prefix_remainders =[]
        for i in nums:
            running += i
            prefix_remainders.append(running%k)
        
        count = 0
        hmap = defaultdict(int)
        for remain in prefix_remainders:
            count+=hmap[remain]
            hmap[remain]+=1
        count+=hmap[0]
        return count