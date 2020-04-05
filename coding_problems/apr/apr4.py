class Solution:
    def reverseWordsInString(self, s: str) -> str:
        s = s.split(' ')
        for i, word in enumerate(s):
            s[i] = word[::-1]

        return ' '.join(s)


def main():
    s = Solution()
    print(s.reverseWordsInString('The cat in the hat'))

if __name__ == '__main__':
    main()