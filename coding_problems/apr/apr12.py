from typing import List

class Solution:
    def getBonuses(self, performance: List[int]) -> List[int]:
        bonuses = [1] * len(performance)
        for i in range(len(performance) - 1):
            if performance[i] > performance[i + 1]:
                bonuses[i] += 1
            elif performance[i + 1] > performance[i]:
                bonuses[i + 1] += 1
        
        return bonuses


def main():
    s = Solution()
    print(s.getBonuses([1, 2, 3, 2, 3, 5, 1]))

if __name__ == '__main__':
    main()