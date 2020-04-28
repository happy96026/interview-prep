class Solution:
    def romanToInt(self, s):
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        prev = 10000
        value = 0
        for c in s:
            value += d[c]
            if prev < d[c]:
                value -= 2 * prev
            prev = d[c]
        
        return value


def main():
    s = Solution()
    print(s.romanToInt('MCMX'))
    print(s.romanToInt('IX'))
    print(s.romanToInt('VII'))
    print(s.romanToInt('MCMIV'))

if __name__ == '__main__':
    main()