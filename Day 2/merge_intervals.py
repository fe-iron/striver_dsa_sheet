class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals) == 1:
            return intervals
        output = []
        intervals.sort()
        output.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] > output[-1][1]:
                output.append(intervals[i])
            else:
                output[-1][1] = max(output[-1][1], intervals[i][1])
        return output
    

sol = Solution()
sol.merge([[1,3],[2,6],[8,10],[15,18]])