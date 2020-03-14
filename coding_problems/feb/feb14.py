class Solution:
  def two_sum(self, l, k):
    s = set()
    for x in l:
      s.add(x)
      if (k -x) in s:
        return True
      
    return False


def main():
  print(Solution().two_sum([4, 7, 1, -3, 2], 5))

if __name__ == '__main__':
  main()