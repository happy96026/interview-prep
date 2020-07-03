class Solution:
    def reverseWords(self, s: str) -> str:
        strList = list(s)
        lo = 0
        hi = len(strList) - 1
        while lo < hi:
            strList[lo], strList[hi] = strList[hi], strList[lo]
            lo += 1
            hi -= 1
        strList.append(' ')

        state = 3
        transitions = [
            {'non-space': 1, 'space': 2},
            {'non-space': 1, 'space': 2},
            {'non-space': 0, 'space': 3},
            {'non-space': 0, 'space': 3},
        ]

        p = 0
        for i, c in enumerate(strList):
            charType = 'space' if c == ' ' else 'non-space'
            state = transitions[state][charType]

            if state == 0:
                lo = i

            elif state == 2:
                low = lo
                hi = i - 1

                while lo < hi:
                    strList[lo], strList[hi] = strList[hi], strList[lo]
                    lo += 1
                    hi -= 1

                for j in range(low, i):
                    strList[p] = strList[j]
                    p += 1

                strList[p] = ' '
                p += 1

        p = max(0, p - 1)
        while len(strList) > p:
            strList.pop()

        return ''.join(strList)


def main():
    s = Solution()
    print(s.reverseWords('the sky is blue'))
    print(s.reverseWords('  hello world!  '))
    print(s.reverseWords('a good  example'))
    print(s.reverseWords('   '))

if __name__ == '__main__':
    main()
