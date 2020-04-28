class Solution:
    def fibonacci(self, n):
        f1 = 0
        f2 = 1

        for i in range(n):
            f1, f2 = f2, f1 + f2

        return f1


def main():
    s = Solution()
    print(s.fibonacci(9))
    print(s.fibonacci(3))
    print(s.fibonacci(7))

if __name__ == '__main__':
    main()