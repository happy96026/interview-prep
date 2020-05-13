from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = []
        for key, val in Counter(nums).items():
            freq.append((-val, key))

        kIndex = k - 1
        lo, hi = 0, len(freq) - 1
        while kIndex != hi:
            pivot = freq[(lo + hi) // 2]
            i, j = lo - 1, hi + 1
            while True:
                while True:
                    i += 1
                    if freq[i] >= pivot: break
                while True:
                    j -= 1
                    if freq[j] <= pivot: break
                
                if i >= j:
                    break

                freq[i], freq[j] = freq[j], freq[i]
            
            if kIndex <= j:
                hi = j
            else:
                freq[lo:j + 1] = sorted(freq[lo:j + 1])
                lo = j + 1

        freq[lo:hi + 1] = sorted(freq[lo:hi + 1])

        return [freq[i][1] for i in range(kIndex + 1)]

def main():
    s = Solution()
    print(s.topKFrequent(['i', 'love', 'leetcode', 'i', 'love', 'coding'], 2))
    print(s.topKFrequent(['i', 'love', 'leetcode', 'i', 'love', 'coding'], 1))
    print(s.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"] , 4))
    print(s.topKFrequent(['daily', 'interview', 'pro', 'pro'], 2))

if __name__ == '__main__':
    main()