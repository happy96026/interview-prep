class Solution:
    def reverse(self, x: int) -> int:
        bound = 2**31 // 10

        reverse = 0
        sign = 1 if x >= 0 else -1
        x *= sign
        while x:
            if (reverse > bound) or (reverse == bound and x > (7 if sign > 0 else 8)):
                return 0

            x, r = divmod(x, 10)
            reverse *= 10
            reverse += r

        return reverse * sign


def main():
    s = Solution()
    print(s.reverse(123))
    print(s.reverse(2**31))
    print(s.reverse(7463847412))

if __name__ == '__main__':
    main()