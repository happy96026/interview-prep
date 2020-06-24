class ListFastSum:
    def __init__(self, nums):
        self.nums = [0]
        for n in nums:
            self.nums.append(self.nums[-1] + n)

    def sum(self, start, end):
        return self.nums[end] - self.nums[start]


def main():
    print(ListFastSum([1, 2, 3, 4, 5, 6, 7]).sum(2, 5))

if __name__ == '__main__':
    main()
