#https://www.hackerrank.com/challenges/sparse-arrays/problem
def matchingStrings(strings, queries):
    
    stringsOccerance = {}
    for string in strings:
        if string in stringsOccerance  :
            stringsOccerance[string] +=1
        else:
            stringsOccerance[string] = 1
    res = []
    for queryStr in queries:
        if queryStr in stringsOccerance:
            res.append(stringsOccerance[queryStr])
        else:
            res.append(0)
    return res
    
