class Solution:
    def longestRun(self, n):
        longest = currRun = 0

        while n > 0:
            n, r = divmod(n, 2)
            if r:
                currRun += 1
                longest = max(longest, currRun)
            else:
                currRun = 0

        return  longest


def main():
    s = Solution()
    print(s.longestRun(242))

if __name__ == '__main__':
    main()