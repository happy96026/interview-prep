class Solution:
  def findPythagoreanTriplets(self, nums):
    for i in range(len(nums)):
      nums[i] *= nums[i]
    nums.sort()
    for k in range(2, len(nums)):
      i = 0
      j = k - 1
      while (i < j):
        s = nums[i] + nums[j]
        if s < nums[k]:
          i += 1
        elif s > nums[k]:
          j -= 1
        else:
          return True
    
    return False


def main():
  s = Solution()
  print(s.findPythagoreanTriplets([3, 12, 5, 13]))

if __name__ == '__main__':
  main()