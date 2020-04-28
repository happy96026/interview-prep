from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        count = 0
        for j in range(len(chars)):
            count += 1
            if j + 1 == len(chars) or chars[j] != chars[j + 1]:
                chars[i] = chars[j]
                i += 1
                if count > 1:
                    for digit in str(count):
                        chars[i] = digit
                        i += 1
                count = 0

        return i


def main():
    s = Solution()
    print(s.compress(['a', 'a', 'b', 'c', 'c', 'c']))
    print(s.compress(['a', 'a', 'b' ,'b', 'c' ,'c' ,'c']))
    print(s.compress(['a']))
    print(s.compress(['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']))

if __name__ == '__main__':
    main()