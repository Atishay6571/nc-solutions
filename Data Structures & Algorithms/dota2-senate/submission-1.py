class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # The key insight is that a senator should always 
        # ban the nearest opposing senator who would otherwise 
        # act before them

        radiants = deque()
        dires = deque()
        n=len(senate)
        for i in range(n):
            if senate[i]=="R":
                radiants.append(i)
            else:
                dires.append(i)
        while radiants and dires:
            rad_senator = radiants.popleft()
            dir_senator = dires.popleft()
            if rad_senator < dir_senator:
                radiants.append(rad_senator+n)
            else:
                dires.append(dir_senator+n)
        if radiants:
            return "Radiant"
        else:
            return "Dire"
