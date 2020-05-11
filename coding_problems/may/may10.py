from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        arr = []
        addOne = 1
        for d in reversed(digits):
            addOne, d = divmod(d + addOne, 10)
            arr.append(d)

        if addOne:
            arr.append(1)

        return arr[::-1]


def main():
    s = Solution()
    print(s.plusOne([1, 2, 3]))
    print(s.plusOne([4, 3, 2, 1]))

if __name__ == '__main__':
    main()