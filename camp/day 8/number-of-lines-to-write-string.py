#https://leetcode.com/contest/weekly-contest-77/problems/number-of-lines-to-write-string/
class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:

        lines = 0
        units = 0
        i = 0
        while i < len(S):
            index = ord(S[i]) - 97
            units += widths[index]
            if units > 100:
                lines += 1
                units = widths[index]
            i+=1
        if units:
            lines += 1            
        return [lines,units]
