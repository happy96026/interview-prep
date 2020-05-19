from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        addresses = []

        def validateBlock(block):
            return int(block) < 256 and (len(block) == 1 or block[0] != '0')
                
        def restoreIpAddresses(currStr='', start=0, count=4):
            if not (count <= len(s) - start <= count * 3):
                return

            if count == 1:
                block = s[start:len(s)]
                if validateBlock(block):
                    addresses.append(currStr + block)
                return

            block = ''
            for i in range(start, min(start + 3, len(s))):
                block += s[i]
                if not validateBlock(block):
                    break

                restoreIpAddresses(currStr + block + '.', i + 1, count - 1)

        restoreIpAddresses()

        return addresses


def main():
    s = Solution()
    print(s.restoreIpAddresses('25525511135'))
    print(s.restoreIpAddresses('1592551013'))
    print(s.restoreIpAddresses('00000'))
    print(s.restoreIpAddresses('010010'))

if __name__ == '__main__':
    main()