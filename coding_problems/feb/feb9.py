class Solution:
  def longestPalindrome(self, s):
    start = 0
    end = 0

    for x in range(2*len(s) - 1):
      i = x >> 1
      j = (x + 1) >> 1
      while i >= 0 and j < len(s) and s[i] == s[j]:
        if end - start + 1 < j - i + 1:
          start = i
          end = j
        i -= 1
        j += 1

    return s[start:end + 1]

s = 'tracecars'
print(str(Solution().longestPalindrome(s)))