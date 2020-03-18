from typing import List

class Solution:
    # def trap(self, height: List[int]) -> int:
    #     '''
    #     Dynamic Programming
    #     Time Complexity: O(n)
    #     Space Complexity: O(n)
    #     '''
    #     waterHeight = []
    #     maxHeight = 0
    #     for h in height:
    #         maxHeight = max(maxHeight, h)
    #         waterHeight.append(maxHeight)

    #     maxHeight = 0
    #     for i in reversed(range(len(height))):
    #         h = height[i]
    #         maxHeight = max(maxHeight, h)
    #         waterHeight[i] = min(waterHeight[i], maxHeight)

    #     trapped = 0
    #     for i in range(len(height)):
    #         trapped += waterHeight[i] - height[i]

    #     return trapped

    # def trap(self, height: List[int]) -> int:
    #     '''
    #     Stack
    #     Time Complexity: O(n)
    #     Space Compleixty: O(n)
    #     '''
    #     stack = []
    #     total = 0
    #     for j in range(len(height)):
    #         while stack and height[stack[-1]] < height[j]:
    #             i = stack.pop()
    #             if not stack:
    #                 break
    #             dist = j - stack[-1] - 1
    #             waterHeight = min(height[stack[-1]], height[j]) - height[i]
    #             total += waterHeight * dist

    #         stack.append(j)

    #     return total

    def trap(self, height: List[int]) -> int:
        '''
        Two Pointers
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        if len(height) < 1:
            return 0

        i, j = 0, len(height) - 1
        leftMax, rightMax = height[i], height[j]
        total = 0

        while i < j:
            if leftMax <= rightMax:
                total += leftMax - height[i]
                i += 1
                leftMax = max(leftMax, height[i])
            else:
                total += rightMax - height[j]
                j -= 1
                rightMax = max(rightMax, height[j])

        return total


def main():
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(s.trap([0, 1, 2, 3]))
    print(s.trap([]))
    print(s.trap([3, 2, 1, 0, 1, 2, 3]))
    print(s.trap([4, 2, 0, 3, 2, 5]))

if __name__ == '__main__':
    main()