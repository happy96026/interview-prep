class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        n = add = 0
        for c in s:
            n += 1 if c == '(' else -1
            if n < 0:
                n = 0
                add += 1

        return add + (n if n > 0 else 0)


def main():
    s = Solution()
    print(s.minAddToMakeValid('())'))
    print(s.minAddToMakeValid('((('))
    print(s.minAddToMakeValid('()'))
    print(s.minAddToMakeValid('()))(('))
    print(s.minAddToMakeValid('(()()'))

if __name__ == '__main__':
    main()
