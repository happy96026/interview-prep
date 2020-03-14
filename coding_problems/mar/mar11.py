from typing import List
import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        minPrice = math.inf
        for price in prices:
            minPrice = min(minPrice, price)
            result = max(result, price - minPrice)

        return result


def main():
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit([7, 6, 4, 3, 1]))
    print(s.maxProfit([9, 11, 8, 5, 7, 10]))

if __name__ == '__main__':
    main()