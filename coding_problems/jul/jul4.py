from typing import List, Dict
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sDict = Counter(s[:len(p)])
        pDict = Counter(p)

        anagrams = [] 
        if self.checkIfAnagram(sDict, pDict):
            anagrams.append(0)

        for i in range(len(s) - len(p)):
            sDict[s[i]] -= 1
            sDict[s[i + len(p)]] += 1
            if self.checkIfAnagram(sDict, pDict):
                anagrams.append(i + 1)

        return anagrams

    def checkIfAnagram(self, s: Dict[str, int], p: Dict[str, int]) -> bool:
        for k, v in p.items():
            if s[k] != v:
                return False

        return True


def main():
    s = Solution()
    print(s.findAnagrams('cbaebabacd', 'abc'))
    print(s.findAnagrams('abab', 'ab'))
    print(s.findAnagrams('acdbacdacb', 'abc'))

if __name__ == '__main__':
    main()
