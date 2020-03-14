class Solution:
  def uniquePaths(self, m, n):
    grid = [[1 for _ in range(n)] for _ in range(m)]

    for i in range(1, m):
      for j in range(1, n):
        grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

    return grid[m - 1][n - 1]


def main():
  s = Solution()
  print(s.uniquePaths(3, 3))

if __name__ == '__main__':
  main()