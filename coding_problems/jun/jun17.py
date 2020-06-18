from collections import Counter

class Solution:
    def isPalindrome(self, s: str) -> str:
        c = Counter(s)

        oddChar = ''
        palindrome = ''
        for k, v in c.items():
            if v % 2 == 1:
                if oddChar:
                    return None
                oddChar = k
            else:
                half = v // 2
                palindrome += k * half
                c[k] = half

        palindrome += oddChar * c[oddChar]
        for k, v in reversed(c.items()):
            if k != oddChar:
                palindrome += k * v
                
        return palindrome


def main():
    s = Solution()
    print(s.isPalindrome('momom'))
    print(s.isPalindrome('ab'))
    print(s.isPalindrome(''))

if __name__ == '__main__':
    main()
