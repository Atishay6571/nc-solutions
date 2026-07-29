class Solution:
    def maxTurbulenceSize(self, arr):
        if len(arr) == 1:
            return 1
        max_len = 1
        curr = 1
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                sign = 1
            elif arr[i] < arr[i-1]:
                sign = -1
            else:
                sign = 0
            
            if i == 1:
                prev_sign = sign
                if sign != 0:
                    curr = 2
                continue
            
            if sign != 0 and sign != prev_sign:
                curr += 1           # alternates → extend
            elif sign != 0:
                curr = 2            # same sign → restart with this pair
            else:
                curr = 1            # equal → reset to single element
            
            max_len = max(max_len, curr)
            prev_sign = sign
        
        return max(max_len, curr)

                

                