class Solution:
    def convertToTitle(self, n):
        title = ''

        while n > 0:
            n, r = divmod(n - 1, 26)
            title += chr(65 + r)

        return title[::-1]


def main():
    s = Solution()
    print(s.convertToTitle(26))
    print(s.convertToTitle(27))
    print(s.convertToTitle(28))

if __name__ == '__main__':
    main()