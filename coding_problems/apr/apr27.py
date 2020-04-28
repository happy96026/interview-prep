import heapq
from collections import Counter

class Solution:
    # def reorganizeString(self, S: str) -> str:
    #     d = {}
    #     for c in S:
    #         d[c] = d.get(c, 0) - 1

    #     heap = [(v, k) for k, v in d.items()]
    #     heapq.heapify(heap)

    #     string = []
    #     prev = None
    #     while heap:
    #         count, char = heapq.heappop(heap)
    #         string.append(char)
    #         count += 1

    #         if prev:
    #             heapq.heappush(heap, prev)
    #             prev = None
    #         if count < 0:
    #             prev = (count, char)
        
    #     if prev:
    #         return ''

    #     return ''.join(string)

    def reorganizeString(self, S: str) -> str:
        counter = Counter()
        maxChar = 'a'
        for c in S:
            counter[c] += 1
            maxChar = max(c, maxChar, key=lambda x: counter[x])

        if counter[maxChar] > (len(S) + 1) // 2:
            return ''
        
        maxFreq = counter[maxChar]
        arr = [maxChar] * maxFreq
        counter.pop(maxChar)

        i = 0
        for char in counter:
            for _ in range(counter[char]):
                arr[i % maxFreq] += char
                i += 1
        
        return ''.join(arr)
        

def main():
    s = Solution()
    print(s.reorganizeString('aab'))
    print(s.reorganizeString('aaab'))
    print(s.reorganizeString('abbccc'))

if __name__ == '__main__':
    main()