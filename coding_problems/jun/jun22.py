class Solution:
    def partitionList(self, nums, k):
        i = 0
        j = len(nums) - 1
        while True:
            while nums[i] < k:
                i += 1
            while nums[j] > k:
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        return nums


def main():
    s = Solution()
    print(s.partitionList([2, 2, 2, 5, 2, 2, 2, 2, 5], 3))

if __name__ == '__main__':
    main()
