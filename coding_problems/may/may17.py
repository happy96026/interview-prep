class Solution:
    def convertToTitle(self, n: int) -> str:
        title = ''

        while n > 0:
            n, r = divmod(n - 1, 26)
            title += chr(65 + r)

        return title[::-1]


def main():
    s = Solution()
    print(s.convertToTitle(27))
    print(s.convertToTitle(51))
    print(s.convertToTitle(52))
    print(s.convertToTitle(676))
    print(s.convertToTitle(702))
    print(s.convertToTitle(704))
    print(s.convertToTitle(1))
    print(s.convertToTitle(28))
    print(s.convertToTitle(701))

if __name__ == '__main__':
    main()