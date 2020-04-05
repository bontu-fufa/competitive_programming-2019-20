#https://leetcode.com/problems/reorganize-string/
import heapq
import operator
class Solution:
    def reorganizeString(self, S: str) -> str:
        letterCount = {}
        
        for letter in S:
            if letter in letterCount:
                letterCount[letter]-=1
            else:
                letterCount[letter]=-1
                

        counted = []
        for key,value in letterCount.items():
            counted.append((value,key))


        heapq.heapify(counted)
        if -(counted[0][0])> math.ceil(len(S)/2): return ""
        
        reorganizedString = []

        while len(counted) >= 2:
            print()
            count1 , firstLetter = heapq.heappop(counted)
            count2 , secondLetter = heapq.heappop(counted)
            reorganizedString.append(firstLetter)
            reorganizedString.append(secondLetter)
            if count1+1:
                heapq.heappush(counted,(count1+1,firstLetter))
            if count2+1:
                heapq.heappush(counted,(count2+1 , secondLetter))
        if counted:
            reorganizedString.append(counted[0][1])


        return "".join(reorganizedString) 
                               
                               
                               
                               
                               
                    

            
