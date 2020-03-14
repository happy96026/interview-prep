from functools import reduce

class Solution:
  def singleNumber(self, nums):
    return reduce(lambda x, y: x ^ y, nums)


def main():
  print(Solution().singleNumber([17, 12, 5, -6, 12, 4, 17, -5, 2, -3, 2, 4, 5, 16, -3, -4, 15, 15, -4, -5, -6]))

if __name__ == '__main__':
  main()