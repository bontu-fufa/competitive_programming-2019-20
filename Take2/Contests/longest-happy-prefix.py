# O(N-1) - space Complexity and  O(N * N-1) compexity
class Solution:
    def longestPrefix(self, s: str) -> str:
        
        maxString = currentPre = currentSuf = ""
        pre = 0
        suf = len(s) - 1
        
        while pre < len(s)-1 and suf > 0:
            currentPre += s[pre]
            currentSuf = s[suf] + currentSuf
            if currentPre == currentSuf and len(currentPre) >= len(maxString):
                maxString = currentPre
            pre += 1
            suf -= 1
        return maxString
                

# O(N) - time Complexity and space compexity

class Solution:
    def longestPrefix(self, s: str) -> str:
        #longestPrefixSuffix dp
        lps = [0] * len(s)
        
        j = 0
        i = 1
        while i < len(s):
            if s[i] == s[j]:
                j += 1
                lps[i] = j
            elif j > 0 : 
                j = lps[j-1]
                i -= 1
            i += 1
        return s[:j]
