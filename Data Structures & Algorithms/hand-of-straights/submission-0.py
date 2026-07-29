class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #brute forcee solution
        if not hand:
            return False
        hand.sort()
        while hand:
            start=hand[0]
            hand.remove(start)
            for i in range(groupSize-1):
                if start+1 in hand:
                    hand.remove(start+1)
                    start+=1
                else:
                    return False
        return True