from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        BYTE_MASKS = [
            None,
            0b10000000,
            0b11100000,
            0b11110000,
            0b11111000
        ]
        BYTE_EQUALS = [
            None,
            0b00000000,
            0b11000000,
            0b11100000,
            0b11110000
        ]

        data.append(0)

        currByte = 0
        currLen = 1
        for byte in data:
            if byte & 0b11000000 != 0b10000000:
                if currLen > 4 or currByte & BYTE_MASKS[currLen] != BYTE_EQUALS[currLen]:
                    return False
                currByte = byte
                currLen = 0
            currLen += 1

        return True


def main():
    s = Solution()
    print(s.validUtf8([0b00000000]))
    print(s.validUtf8([0b00000000, 0b10000000]))
    print(s.validUtf8([0b11000000, 0b10000000]))
    print(s.validUtf8([0b11000101, 0b10000010, 0b00000001]))
    print(s.validUtf8([240, 162, 138, 147, 145]))

if __name__ == '__main__':
    main()
