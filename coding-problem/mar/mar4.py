class Solution:
    def witnesses(self, heights):
        result = 0
        max_height = 0
        for n in reversed(heights):
            if n > max_height:
                result += 1
                max_height = n

        return result

def main():
    s = Solution()
    print(s.witnesses([2, 1]))

if __name__ == '__main__':
    main()