import unittest

class Solution(unittest.TestCase):
    def base2(self, n: int) -> str:
        arr = []
        while n > 0:
            n, r = divmod(n, 2)
            arr.append(str(r))

        arr.reverse()
        return ''.join(arr)

    def test_1(self):
        self.assertEqual(self.base2(123), '1111011')


def main():
    unittest.main()

if __name__ == '__main__':
    main()
