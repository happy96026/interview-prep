class Solution:
    def singleNumber(self, nums):
        x = 0
        for n in nums:
            x ^= n
        
        return x


def main():
    s = Solution()
    print(s.singleNumber([7, 3, 5, 5, 4, 3, 4, 8, 8]))
    print(s.singleNumber([1, 1, 3, 4, 4, 5, 6, 5, 6]))

if __name__ == '__main__':
    main()