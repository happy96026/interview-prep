class Solution:
  def sortNums(self, nums):
    d = {}
    for x in nums:
      if x not in d:
        d[x] = 0
      d[x] += 1
    
    uniqueNums = sorted(d.keys())
    i = 0
    for num in uniqueNums:
      occ = d[num]
      for _ in range(occ):
        nums[i] = num
        i += 1
    
    return nums

def main():
  print(Solution().sortNums([3, 3, 2, 1, 3, 2, 1]))
  pass

if __name__ == '__main__':
  main()