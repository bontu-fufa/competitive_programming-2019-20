#https://leetcode.com/problems/first-bad-version
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def middler(i,f):

            mid =(i + f)//2

            if isBadVersion(mid) and not isBadVersion(mid-1) :
                return mid
            if isBadVersion(mid):
                return middler(i,mid)
            else :
                return middler(mid,f)


        return(middler(0,n+1))
