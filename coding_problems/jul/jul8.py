class Solution:
    def pow(self, x: float, n: int) -> float:
        isMinus = False
        if n < 0:
            n *= -1
            isMinus = True
            
        result = 1
        while n > 0:
            n, r = divmod(n, 2)
            if r:
                result *= x
            x *= x
            
        return 1 / result if isMinus else result
        


def main():
    s = Solution()
    print(s.pow(5, 13))

if __name__ == '__main__':
    main()
