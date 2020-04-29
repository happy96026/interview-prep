from typing import List
import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def comparator(a, b):
            return int(b + a) - int(a + b)

        nums = sorted([str(n) for n in nums], key=functools.cmp_to_key(comparator))

        return str(int(''.join([str(n) for n in nums])))


def main():
    s = Solution()
    print(s.largestNumber([17, 7, 2, 45, 72]))
    print(s.largestNumber([10, 2]))
    print(s.largestNumber([3, 30, 34, 5, 9]))
    print(s.largestNumber([0, 0, 0, 1]))
    print(s.largestNumber([0, 0, 0, 0]))
    print(s.largestNumber([123, 1232]))
    print(s.largestNumber([121, 12]))

if __name__ == '__main__':
    main()