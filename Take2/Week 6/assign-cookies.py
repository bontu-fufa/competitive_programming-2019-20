#https://leetcode.com/problems/assign-cookies/
def findContentChildren(self, g: List[int], s: List[int]) -> int:
    g , s = sorted(g) , sorted(s)
    output,i,j = 0,0,0
    while i < len(g) and j < len(s):
        if g[i] > s[j]:
            j += 1
        else:
            output += 1
            i += 1
            j += 1
    return output
