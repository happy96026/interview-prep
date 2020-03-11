# O(n)
class Solution0:
  def getRange(self, arr, target):
    result = [-1, -1]
    found = False
    for i, x in enumerate(arr):
      if x == target:
        if result[0] == -1: result[0] = i
        result[1] = i
      elif result[0] > -1:
        return result

    return result

# O(log n)
class Solution:
  def getRange(self, arr, target):
    i = self.getFarthest(arr, target, 0)
    if i == -1:
      return [-1, -1]
    
    return [i, self.getFarthest(arr, target, i, False)]

  def getFarthest(self, arr, target, i, left=True):
    j = len(arr)
    while i < j:
      m = (i + j) // 2
      if arr[m] > target or (left and arr[m] == target): j = m
      else: i = m + 1

    if not left: i -= 1
    if i < len(arr) and arr[i] == target: return i
    return -1

def main():
  arr_list = [
    {'A': [1, 3, 3, 5, 7, 8, 9, 9, 9, 15], 'target': 9},
    {'A': [100, 150, 150, 153], 'target': 150},
    {'A': [1, 2, 3, 4, 5, 6, 10], 'target': 9},
    {'A': [1, 2, 2, 2, 2, 3, 4, 7, 8, 8], 'target': 2},
  ]
  sol0 = Solution0()
  sol = Solution()

  for test in arr_list:
    a = test['A']
    target = test['target']
    print(sol.getRange(a, target))

if __name__ == '__main__':
  main()