class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        elif not A and not B:
            return True

        table = [0] * len(A)
        for i in range(len(A) - 1):
            if A[table[i]] == A[i + 1]:
                table[i + 1] = table[i] + 1

        i = j = 0
        while j < len(B) * 2:
            if A[i] == B[j % len(B)]:
                if i == len(A) - 1:
                    return True
                i += 1
                j += 1
            elif i == 0:
                j += 1
            else:
                i = table[i - 1]
                
        return False


def main():
    s = Solution()
    # print(s.rotateString('abcde', 'cdeab'))
    # print(s.rotateString('abcde', 'abced'))
    print(s.rotateString('bbbacddceeb','ceebbbbacdd'))
    # print(s.rotateString('bba', 'bbba'))

if __name__ == '__main__':
    main()