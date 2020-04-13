#https://leetcode.com/problems/delete-columns-to-make-sorted
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        delet = 0
        for c in range(len(A[0])):
            for r in range(len(A)-1):
                if A[r][c] > A[r+1][c]:
                    delet +=1
                    break
        return delet
