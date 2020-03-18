class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False

        diff = []
        s = set()
        repeatChar = False
        for i in range(len(A)):
            if A[i] != B[i]:
                diff.append(i)
            if A[i] in s:
                repeatChar = True

            s.add(A[i])
            
        if len(diff) == 0 and repeatChar:
            return True
        elif len(diff) == 2:
            i, j = diff
            return A[i] == B[j] and A[j] == B[i]
        else:
            return False


def main():
    s = Solution()
    print(s.buddyStrings('ab', 'ba'))
    print(s.buddyStrings('ab', 'ab'))
    print(s.buddyStrings('aa', 'aa'))
    print(s.buddyStrings('aaaaaaabc', 'aaaaaaacb'))
    print(s.buddyStrings('', 'aa'))

if __name__ == '__main__':
    main()