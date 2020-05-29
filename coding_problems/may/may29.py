class Solution:
    KAPREKAR_CONSTANT = 6174

    def numKaprekarIterations(self, n):
        i = 0

        while n != self.KAPREKAR_CONSTANT:
            i += 1
            asc = sorted(str(n))
            desc = asc[::-1]
            desc += ['0'] * (4 - len(desc))
            n = int(''.join(desc)) - int(''.join(asc))

        return i


def main():
    s = Solution()
    print(s.numKaprekarIterations(123))

if __name__ == '__main__':
    main()
