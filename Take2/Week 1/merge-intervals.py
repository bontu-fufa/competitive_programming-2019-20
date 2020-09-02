#https://leetcode.com/problems/merge-intervals
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) < 2: return intervals
    intervals = sorted(intervals)
    output = [intervals[0]]
    for initial,final in  intervals[1:]:
        if output[-1][1] < initial:
            output.append([initial,final])
        else:
            output[-1][1] = max(final,output[-1][1])
    return output
