from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1]
        for n in nums[:-1]:
            products.append(n * products[-1])

        product = 1
        for i in reversed(range(1, len(nums))):
            product *= nums[i]
            products[i - 1] *= product

        return products

def main():
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))
    print(s.productExceptSelf([1, 2, 3, 4, 5]))

if __name__ == '__main__':
    main()