class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        if K == 0:
            return 1

        moves = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]
        dp = [[1] * N for _ in range(N)]

        totalMoves = 1
        for _ in range(K):
            totalMoves *= len(moves)
            new_dp = [[0] * N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    noMoves = 0
                    for a, b in moves:
                        new_i = i + a
                        new_j = j + b
                        noMoves += dp[new_i][new_j] if 0 <= new_i < N and 0 <= new_j < N else 0
                    new_dp[i][j] = noMoves

            dp = new_dp

        return dp[r][c] / totalMoves


def main():
    s = Solution()
    print(s.knightProbability(3, 3, 0, 0))

if __name__ == '__main__':
    main()
