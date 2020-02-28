#https://leetcode.com/problems/maximum-length-of-pair-chain
import operator
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs = sorted(pairs, key = operator.itemgetter(1))
        print(pairs)
        count = 0
        point = float("-inf")
        for i in range(len(pairs)):

            if point < pairs[i][0]:
                point = pairs[i][1]
                count+=1
        return count
