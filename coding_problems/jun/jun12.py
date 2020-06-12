from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = set(['+', '-', '*', '/'])
        if not tokens:
            return 0

        stack = []
        for token in tokens:
            if token in operands:
                n2 = stack.pop()
                n1 = stack.pop()

                if token == '+':
                    stack.append(n1 + n2)
                elif token == '-':
                    stack.append(n1 - n2)
                elif token == '*':
                    stack.append(n1 * n2)
                else:
                    stack.append(int(n1 / n2))
            else:
                stack.append(int(token))

        return stack.pop()


def main():
    s = Solution()
    print(s.evalRPN(['2', '1', '+', '3', '*']))
    print(s.evalRPN(['4', '13', '5', '/', '+']))
    print(s.evalRPN(['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']))

if __name__ == '__main__':
    main()
