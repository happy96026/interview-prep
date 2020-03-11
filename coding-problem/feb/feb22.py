from typing import Dict, Tuple

class Solution:
  def minDistance(self, word1: str, word2: str, d: Dict[Tuple[str, str], int] = {}) -> int:
    if (word1, word2) not in d:
      if min(len(word1), len(word2)) == 0:
        d[(word1, word2)] = max(len(word1), len(word2))
      else:
        d[(word1, word2)] = min(
          self.minDistance(word1[:-1], word2) + 1,
          self.minDistance(word1, word2[:-1]) + 1, 
          self.minDistance(word1[:-1], word2[:-1]) + (1 if word1[-1] != word2[-1] else 0)
        )
    
    return d[(word1, word2)]


def main():
  s = Solution()
  print(s.minDistance('horse', 'ros'))
  print(s.minDistance('intention', 'execution'))
  
if __name__ == '__main__':
  main()