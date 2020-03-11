from typing import List

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = True
        if (dividend >= 0 and divisor < 0) or (dividend < 0 and divisor >= 0):
            positive = False
        
        quotient = 0
        if dividend >= 0:
            while dividend >= 0:
                if positive:
                    quotient += 1
                    dividend -= divisor
                else:
                    quotient -= 1
                    dividend += divisor
        else:
            while dividend <= 0:
                if positive:
                    quotient += 1
                    dividend -= divisor
                else:
                    quotient -= 1
                    dividend += divisor
            
        return quotient + (-1 if positive else 1)
        

def main():
    s = Solution()
    print(s.divide(-2147483648, -2))

if __name__ == '__main__':
    main()