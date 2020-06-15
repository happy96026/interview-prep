from typing import List

class TrieNode:
    def __init__(self, val):
        self.children = {}
        self.val = val

class Solution:
    def shortestUniquePrefix(self, words: List[str]) -> List[str]:
        trie = self.buildTrie(words)
        prefixes = []
        print(trie.children)

        for word in words:
            arr = []
            node = trie
            for c in word:
                node = node.children[c]
                arr.append(c)
                if len(node.children) <= 1:
                    break
            prefixes.append(''.join(arr))

        return prefixes

    def buildTrie(self, words: List[str]) -> TrieNode:
        root = TrieNode('')

        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode(c)
                node = node.children[c]

        return root


def main():
    s = Solution()
    print(s.shortestUniquePrefix(['joma', 'john', 'jack', 'techlead']))

if __name__ == '__main__':
    main()
