class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        taken = set()

        for i in range(len(s)):
            if s[i] not in d:
                if t[i] in taken:
                    return False
                d[s[i]] = t[i]
                taken.add(t[i])

            elif d[s[i]] != t[i]:
                return False

        return True


def main():
    s = Solution()
    print(s.isIsomorphic('egg', 'add'))
    print(s.isIsomorphic('foo', 'bar'))
    print(s.isIsomorphic('paper', 'title'))
    print(s.isIsomorphic('abc', 'def'))
    print(s.isIsomorphic('aab', 'def'))

if __name__ == '__main__':
    main()
