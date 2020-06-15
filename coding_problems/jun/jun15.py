class Solution:
    def firstRecurringChar(self, s):
        _set = set()
        for c in s:
            if c in _set:
                return c
            _set.add(c)

        return None


def main():
    s = Solution()
    print(s.firstRecurringChar('qwertty'))
    print(s.firstRecurringChar('qwerty'))

if __name__ == '__main__':
    main()
