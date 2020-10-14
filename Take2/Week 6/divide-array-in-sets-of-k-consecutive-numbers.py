def isPossibleDivide(self, nums: List[int], k: int) -> bool:
    nums.sort()
    numsOcc = {}

    for num in nums:
        if num not in numsOcc:numsOcc[num] = 1
        else:numsOcc[num] += 1

    for n in nums:
        if numsOcc[n] != 0:
            occ = numsOcc[n]
            for i in range(n,n+k):
                if i not in numsOcc: return False

                numsOcc[i] -= occ
                if numsOcc[i] < 0: return False
    return True
