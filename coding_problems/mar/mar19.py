class Solution:
    '''
    Time Complexity: O(n * MAX_LEN)
    Space Complexity: O(MAX_LEN)
    '''
    def countAndSay(self, n: int) -> str:
        currCountAndSay = [1]
        for _ in range(1, n):
            nextCountAndSay = []

            for c in currCountAndSay:
                if len(nextCountAndSay) > 0 and nextCountAndSay[-1] == c:
                    nextCountAndSay[-2] += 1
                else:
                    nextCountAndSay += [1, c]

            currCountAndSay = nextCountAndSay
        print(currCountAndSay)
            
        return ''.join([str(x) for x in currCountAndSay])
            

def main():
    s = Solution()
    print(s.countAndSay(30))

if __name__ == '__main__':
    main()