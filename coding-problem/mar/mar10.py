from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals

        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            curr_interval = intervals[i]
            last_interval = result[-1]
            if curr_interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], curr_interval[1])
            else:
                result.append(curr_interval)

        return result


def main():
    s = Solution()
    print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(s.merge([[1, 4], [4, 5]]))
    print(s.merge([[1, 3], [5, 8], [4, 10], [20, 25]]))
    print(s.merge([[1, 4], [0, 4]]))

if __name__ == '__main__':
    main()