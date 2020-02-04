# https://leetcode.com/problems/unique-number-of-occurrences
def uniqueOccurrences(arr: List[int]) -> bool:
    nums=set(arr)
    count = []
    for i in nums:
        occurance = arr.count(i)
        if occurance not in count:
            count.append(occurance)
        else:
            return False
    return True
