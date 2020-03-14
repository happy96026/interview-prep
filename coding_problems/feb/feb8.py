class Solution:
  def lengthOfLongestString(self, s):
    d = {}
    i = 0
    max_len = 0
    for j, c in enumerate(s):
      if c in d:
        i = max(i, d[c] + 1)
      d[c] = j
      max_len = max(max_len, j - i + 1)

    return max_len

print(Solution().lengthOfLongestString('abrkaabcdefghijjxxx'))