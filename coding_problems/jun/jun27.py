from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        rotates = i = 0
        while rotates < len(nums):
            curr = i
            x = nums[curr]
            while True:
                _next = (curr + k) % len(nums)
                nums[_next], x = x, nums[_next]
                rotates += 1
                if _next == i:
                    break
                curr = _next
            i += 1


def main():
    s = Solution()

    arr = [1, 2, 3, 4, 5, 6, 7]
    print(s.rotate(arr, 3))
    print(arr)

    arr = [-1, -100, 3, 99]
    print(s.rotate(arr, 2))
    print(arr)

    arr = [-1, -100, 3, 99]
    print(s.rotate(arr, 1))
    print(arr)

if __name__ == '__main__':
    main()
