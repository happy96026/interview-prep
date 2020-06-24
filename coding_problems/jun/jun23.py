from typing import List
import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        dp[0] = 0
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] = min(dp[i], dp[i - c] + 1)

        return dp[amount] if dp[amount] != math.inf else -1


def main():
    s = Solution()
    print(s.coinChange([1, 2, 5], 11))
    print(s.coinChange([2], 3))

if __name__ == '__main__':
    main()
