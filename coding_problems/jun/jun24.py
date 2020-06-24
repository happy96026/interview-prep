from typing import List
from collections import defaultdict

class Solution:
    def makeWords(self, validWords: List[str], phone: str) -> List[str]:
        numbersMap = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }
        lettersMap = {}
        for n, arr in numbersMap.items():
            for c in arr:
                lettersMap[c] = n

        d = defaultdict(list)
        for word in validWords:
            numbers = ''.join([str(lettersMap[c]) for c in word])
            d[numbers].append(word)

        return d[phone]


def main():
    s = Solution()
    print(s.makeWords(['dog', 'fish', 'cat', 'fog'], '364'))

if __name__ == '__main__':
    main()
