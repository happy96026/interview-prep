class Solution:
  def check(self, nums):
    modified = False
    for i in range(len(nums) - 1):
      if nums[i] > nums[i + 1]:
        if modified:
          return False
        elif i - 1 >= 0 and nums[i - 1] > nums[i + 1]:
          nums[i + 1] = nums[i]
        modified = True

    return True

def main():
  s = Solution()
  # print(s.check([13, 4, 7]))
  # print(s.check([5, 1, 3, 2, 5]))
  print(s.check([-1, 4, 2, 3]))

if __name__ == '__main__':
  main()