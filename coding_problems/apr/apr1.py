import string
import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Hash
        n is the length of array and m is the length of str
        Time Complexity: O(nklogk)
        Space Complexity: O(nk)
        '''
        d = collections.defaultdict(list)
        for s in strs:
            sortedString = ''.join(sorted(s))
            d[sortedString].append(s)

        return list(d.values())

    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     '''
    #     Count Character Occurences
    #     n in the length of array and m is the length of str
    #     Time Complexity: O(nk)
    #     Space Complexity: O(nk)
    #     '''
    #     d = collections.defaultdict(list)
    #     for s in strs:
    #         l = [0] * 26
    #         for c in s:
    #             l[ord(c) - ord('a')] += 1
    #         d[tuple(l)].append(s)

    #     return list(d.values())


def main():
    s = Solution()
    print(s.groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
    print(s.groupAnagrams(['abc', 'bcd', 'cba', 'cbd', 'efg']))

if __name__ == '__main__':
    main()