class Solution:
    def swapBits(self, n: int) -> int:
        return 0 ^ (0b01010101010101010101010101010101 & n >> 1) ^ (0b10101010101010101010101010101010 & n << 1)


def main():
    s = Solution()
    print(f'0b{s.swapBits(0b10101010101010101010101010101010):032b}')

if __name__ == '__main__':
    main()
