class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        y = x
        z = 0
        while True:
            y, r = divmod(y, 10)
            z += r
            if y == 0:
                break
            z *= 10

        return x == z


def main():
    s = Solution()
    print(s.isPalindrome(121))
    print(s.isPalindrome(-121))
    print(s.isPalindrome(10))
    print(s.isPalindrome(1234321))
    print(s.isPalindrome(1234322))

if __name__ == '__main__':
    main()
