class Solution:
  def staircase(self, n, d={}):
    if n not in d:
      if n <= 2:
        d[n] = n
      else:
        d[n] = self.staircase(n - 1) + self.staircase(n - 2)

    return d[n]

def main():
  s = Solution()
  print(s.staircase(4))
  print(s.staircase(5))

if __name__ == '__main__':
  main()