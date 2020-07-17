import unittest

class Solution(unittest.TestCase):
    def removeOuterParentheses(self, S: str) -> str:
        result = ''
        prev = curr = 0
        for c in S:
            curr += 1 if c == '(' else -1
            if not ((prev == 0 and curr == 1) or (prev == 1 and curr == 0)):
                result += c
            prev = curr

        return result

    def test_1(self):
        self.assertEqual(self.removeOuterParentheses('(()())(())'), '()()()')

    def test_2(self):
        self.assertEqual(self.removeOuterParentheses('(()())(())(()(()))'), '()()()()(())')

    def test_3(self):
        self.assertEqual(self.removeOuterParentheses('()()'), '')


def main():
    unittest.main()

if __name__ == '__main__':
    main()
