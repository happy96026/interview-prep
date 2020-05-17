class Solution:
    def compareVersion(self, version1: str, version2: str):
        version1 = version1.split('.')
        version2 = version2.split('.')

        for i in range(max(len(version1), len(version2))):
            v1 = int(version1[i]) if i < len(version1) else 0
            v2 = int(version2[i]) if i < len(version2) else 0

            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1

        return 0


def main():
    s = Solution()

    print(s.compareVersion('0.1', '1.1'))
    print(s.compareVersion('1.0.1', '1'))
    print(s.compareVersion('7.5.2.4', '7.5.3'))
    print(s.compareVersion('1.01', '1.001'))
    print(s.compareVersion('1.0', '1.0.0'))
    print(s.compareVersion('1.0.33', '1.0.27'))

if __name__ == '__main__':
    main()