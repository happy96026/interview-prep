import re

class Solution:
    def __init__(self):
        self.pattern = re.compile(r'^\s*[+-]?(\d+\.?\d*|\.\d+)(e[+-]?\d+)?\s*$')

    def isNumber(self, s: str) -> bool:
        return self.pattern.match(s)


def main():
    s = Solution()
    print(s.isNumber("1  "))
    print(s.isNumber('1.'))
    print(s.isNumber('.1'))
    print(s.isNumber(''))
    print(s.isNumber('0'))
    print(s.isNumber(' 0.1'))
    print(s.isNumber('abc'))
    print(s.isNumber('1 a'))
    print(s.isNumber('2e10'))
    print(s.isNumber('-90e3'))
    print(s.isNumber(' 1e'))
    print(s.isNumber('e3'))
    print(s.isNumber('6e-1'))
    print(s.isNumber('99e2.5'))
    print(s.isNumber('53.5e93'))
    print(s.isNumber('--6'))
    print(s.isNumber('-+3'))
    print(s.isNumber('95a54e53'))

if __name__ == '__main__':
    main()
