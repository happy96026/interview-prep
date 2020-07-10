class Solution:
    def sqrt(self, x):
        y_i = 1
        while y_i * y_i < x:
            y_i += 1
        
        while True:
            y_j = y_i - (y_i * y_i - x) / (2 * y_i)
            if abs(y_i - y_j) < 0.001:
                break
            y_i = y_j

        return y_j


def main():
    s = Solution()
    print(s.sqrt(1645))

if __name__ == '__main__':
    main()
