# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero
class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        neg = []
        if n == 1:
            return [0]
        
        num = n
        for i in range(n//2):
            neg.append((-(num-i)))

        pos = []
        for i in range(n//2):
            pos.append(-(neg[i]))
        if n%2 == 0:
            return pos + neg
        else :
            return pos + neg  + [0]
