class Solution:
    def longestSubstringWithKDistinct(self, s, k):
        '''
        Sliding Window
        Time Complexity: O(n)
        Space Complexity: O(k)
        '''
        d = {}
        i = result = 0
        for j in range(len(s)):
            if s[j] not in d:
                d[s[j]] = 0
            d[s[j]] += 1

            while len(d) > k:
                d[s[i]] -= 1
                if d[s[i]] == 0:
                    del d[s[i]]
                i += 1

            result = max(result, j - i + 1)

        return result
            

def main():
    s = Solution()
    print(s.longestSubstringWithKDistinct('aabcdefff', 3))
    print(s.longestSubstringWithKDistinct('abcbbbbcccbdddadacb', 2))
    print(s.longestSubstringWithKDistinct('aabacbebebe', 3))
    print(s.longestSubstringWithKDistinct('aabacbebebe', 0))

if __name__ == '__main__':
    main()