#https://leetcode.com/problems/matrix-cells-in-distance-order

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
            M = []
            for i in range(R):
                for j in range(C):
                    M.append([i,j])
        
            di = []
            for i in range(len(M)):
                d = abs(M[i][0] - r0) + abs(M[i][1]-c0)
                di.append([d,i])
            di.sort()
            srt = []
            for i in range(len(di)):

                srt.append(M[di[i][1]])
            return(srt)
