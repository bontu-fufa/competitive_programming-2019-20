#https://leetcode.com/contest/weekly-contest-199/problems/bulb-switcher-iv/

class Solution:
    def minFlips(self, target: str) -> int:
        
        count,prev = 0,target[0]
        
        if prev == "1": count+=1
        
        for i in range(1,len(target)):
            if prev != target[i]:
                count += 1
                prev = target[i]
                
                
        return count
