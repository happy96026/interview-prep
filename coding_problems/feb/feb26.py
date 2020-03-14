# O(n)
# class Solution:
#   def minSubArrayLen(self, nums, s):
#     result = len(nums) + 1
#     _sum = i = 0
#     for j in range(len(nums)):
#       _sum += nums[j]
#       while _sum >= s:
#         result = min(result, j - i + 1)
#         _sum -= nums[i]
#         i += 1
      
#     return result if result <= len(nums) else 0

# O(n log n)
class Solution:
  def minSubArrayLen(self, nums, s):
    result = len(nums) + 1
    sums = [nums[0]]
    for i in range(1, len(nums)):
      sums.append(sums[i - 1] + nums[i])
    
    for i in range(len(nums)):
      target = s + sums[i] - nums[i]
      j = self.binarySearch(sums, target, i, len(sums))
      if j > -1:
        result = min(result, j - i + 1)

    return result if result <= len(nums) else 0

  def binarySearch(self, nums, target, i, j):
    while i < j:
      k = (i + j) // 2
      if nums[k] >= target:
        j = k
      else:
        i = k + 1

    if i >= len(nums):
      return -1
    
    return i if nums[i] >= target else i + 1


def main():
  s = Solution()
  print(s.minSubArrayLen([2, 3, 1, 2, 4, 3], 7))
  print(s.minSubArrayLen([2, 3, 1, 2, 4], 7))
  print(s.minSubArrayLen([0, 1, 5], 7))
  print(s.minSubArrayLen([0, 1000, 5, 4, 2, 7], 7))
  print(s.minSubArrayLen([0, 1000, 5, 4, 2, 7], 7))
  # arr = [2, 5, 6, 8, 12, 15]
  # print(s.binarySearch(arr, 7, 0, len(arr)))

if __name__ == '__main__':
  main()