class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = 0

        for _ in range(32):
            n, r = divmod(n, 2)
            reverse *= 2
            reverse += r

        return reverse


def main():
    s = Solution()
    print(s.reverseBits(0b00000010100101000001111010011100))
    print(s.reverseBits(0b11111111111111111111111111111101))
    print(s.reverseBits(1234))

if __name__ == '__main__':
    main()
