class Solution:
    def findSmallest(self, nums):
        _max = 1
        for n in nums:
            if n > _max:
                break
            _max += n

        return _max


def main():
    s = Solution()
    print(s.findSmallest([1, 2, 3, 8, 9, 10]))
    print(s.findSmallest([1, 3, 6, 19, 11, 15]))
    print(s.findSmallest([1, 1, 1, 1]))
    print(s.findSmallest([1, 1, 3, 4]))
    print(s.findSmallest([1, 2, 5, 10, 20, 40]))
    print(s.findSmallest([1, 2, 3, 4, 5, 6]))

if __name__ == '__main__':
    main()