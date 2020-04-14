#https://www.hackerrank.com/challenges/equality-in-a-array/problem
def equalizeArray(arr):
    total = len(arr)
    maxx = 0
    occurance = {}
    for n in arr:
        if n not in occurance:
            occurance[n] = 1
        else:
            occurance[n] += 1
    maxx = sorted(occurance.items(), key=operator.itemgetter(1))
    return total - (maxx[-1][1])
