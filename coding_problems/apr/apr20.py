from typing import List

class Solution:
    # def hIndex(self, citations: List[int]) -> int:
    #     '''
    #     Sorting
    #     Time Complexity: O(n log n)
    #     Space Complexity: O(1)
    #     '''
    #     citations.sort(reverse=True)
    #     if not citations or citations[0] == 0:
    #         return 0

    #     i = 0
    #     j = len(citations) - 1
    #     while i < j:
    #         mid = (i + j) // 2 + (i + j) % 2
    #         if citations[mid] < mid + 1:
    #             j = mid - 1
    #         elif citations[mid] > mid + 1:
    #             i = mid
    #         else:
    #             return mid + 1

    #     return i + 1

    # def hIndex(self, citations: List[int]) -> int:
    #     '''
    #     Two Pass
    #     Time Complexity: O(n)
    #     Space Complexity: O(n)
    #     '''
    #     arr = [0] * (len(citations) + 1)
    #     for n in citations:
    #         arr[min(len(citations), n)] += 1
        
    #     count = 0
    #     for i in reversed(range(len(arr))):
    #         count += arr[i]
    #         if count >= i:
    #             return i

    def hIndex(self, citations: List[int]) -> int:
        '''
        One Pass
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        arr = [0] * (len(citations) + 1)
        hIndex = 0
        count = 0
        for n in citations:
            index = min(len(citations), n)
            arr[index] += 1
            if index > hIndex:
                count += 1
                if count > hIndex:
                    hIndex += 1
                    count -= arr[hIndex]
        
        return hIndex


def main():
    s = Solution()
    print(s.hIndex([3, 0, 6, 1, 5]))
    print(s.hIndex([3, 5, 0, 1, 3]))
    print(s.hIndex([11, 15]))

if __name__ == '__main__':
    main()