class Solution:
    def insert(self, intervals: List[List[int]],
               newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals

        if intervals[-1][1] < newInterval[0]:
            return intervals + [newInterval]

        res = []
        for i, interval in enumerate(intervals):
            if interval[0] <= newInterval[0] <= interval[1] or interval[
                    0] <= newInterval[1] <= interval[1] or newInterval[
                        0] <= interval[0] <= newInterval[1]:
                newInterval = [
                    min(interval[0], newInterval[0]),
                    max(interval[1], newInterval[1])
                ]

                if i == len(intervals) - 1:
                    res.append(newInterval)

                continue

            if interval[1] < newInterval[0]:
                res.append(interval)
                continue

            if newInterval[1] < interval[0]:
                res.append(newInterval)
                res += intervals[i:]
                break

        return res