from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        '''
        Hash Table
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        if len(words) < 2: return True

        d = { c: i for i, c in enumerate(order) }
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            for i in range(len(word1)):
                if i >= len(word2) or d[word1[i]] > d[word2[i]]:
                    return False
                elif d[word1[i]] < d[word2[i]]:
                    break

        return True


def main():
    s = Solution()

    words = ['hello', 'leetcode']
    order = 'hlabcdefgijkmnopqrstuvwxyz'
    print(s.isAlienSorted(words, order))

    words = ['word', 'world', 'row']
    order = 'worldabcefghijkmnpqstuvxyz'
    print(s.isAlienSorted(words, order))

    words = ['apple', 'app']
    order = 'abcdefghijklmnopqrstuvwxyz'
    print(s.isAlienSorted(words, order))

if __name__ == '__main__':
    main()