from typing import List

class Solution:
    def maxChange(self, m: List[List[int]]) -> int:
        dp = [0] * len(m[0])
        for i in range(len(m)):
            dp[0] += m[i][0]
            for j in range(1, len(m[0])):
                dp[j] = max(dp[j - 1], dp[j]) + m[i][j]

        return dp[-1]


def main():
    s = Solution()
    print(s.maxChange(
        [
            [0, 3, 0, 2],
            [1, 2, 3, 3],
            [6, 0, 3, 2]
        ]
    ))

if __name__ == '__main__':
    main()
