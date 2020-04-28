class Solution:
    # def decodeString(self, s: str) -> str:
    #     stack = []
    #     for c in s:
    #         if c == ']':
    #             curr = ''
    #             while True:
    #                 popped = stack.pop()
    #                 if popped == '[':
    #                     break
    #                 curr = popped + curr

    #             repeat = ''
    #             while stack and stack[-1].isnumeric():
    #                 repeat = stack.pop() + repeat

    #             stack.append(curr * int(repeat))
    #         else:
    #             stack.append(c)

    #     return ''.join(stack)

    def decodeString(self, s: str) -> str:
        numStack = []
        strStack = []
        currNum  = currStr = ''
        for c in s:
            if c == '[':
                numStack.append(int(currNum))
                strStack.append(currStr)
                currNum = currStr = ''
            elif c == ']':
                currStr = strStack.pop() + currStr * numStack.pop()
            elif c.isdigit():
                currNum += c
            else:
                currStr += c

        return currStr


def main():
    s = Solution()
    print(s.decodeString('3[a]2[bc]'))
    print(s.decodeString('3[a2[c]]'))
    print(s.decodeString('2[abc]3[cd]ef'))
    print(s.decodeString('2[a2[b]c]'))
    print(s.decodeString('100[a2[b]c]'))

if __name__ == '__main__':
    main()