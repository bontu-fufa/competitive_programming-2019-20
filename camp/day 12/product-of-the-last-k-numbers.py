#https://leetcode.com/contest/weekly-contest-176/problems/product-of-the-last-k-numbers


class ProductOfNumbers:

    def __init__(self):
        self.myList = []
        self.prod = [1]
        self.zeros = float('-inf')
        

    def add(self, num: int) -> None:
        self.myList.append(num)
        if self.prod[-1] == 0:
            self.zeros= len(self.prod) - 1
            self.prod.append(num)
        else:
            self.prod.append(self.prod[-1] * num)
    def getProduct(self, k: int) -> int:
        index = -1-k    
        if len(self.prod) + index < self.zeros : return 0
        if self.prod[index] ==0 : return self.prod[-1]
        return self.prod[-1] // self.prod[index]
    
    
    
        ## O(n) -- TLE
        # product = 1
        # if len(self.myList) == 1 and k == 1:
        #     return self.myList[0]
        # start = len(self.myList) - k
        # for i in range(start,len(self.myList)):
        #     product *= self.myList[i]
        # return product
