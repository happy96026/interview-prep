from typing import List

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        A = [n * n for n in A]

        res = []
        i = 0
        j = len(A) - 1
        while i <= j:
            if A[i] > A[j]:
                res.append(A[i])
                i += 1
            else:
                res.append(A[j])
                j -= 1

        return res[::-1]

def main():
    s = Solution()
    print(s.sortedSquares([-4, -1, 0, 3, 10]))
    print(s.sortedSquares([-7, -3, 2, 3, 11]))

if __name__ == '__main__':
    main()
