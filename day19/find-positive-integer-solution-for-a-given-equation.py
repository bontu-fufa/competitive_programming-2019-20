https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        result = []
        
        for i in range(1,z+1):
            for j in range(1,z+1):
                if customfunction.f(i,j) == z:
                    result.append([i,j])
        return result
