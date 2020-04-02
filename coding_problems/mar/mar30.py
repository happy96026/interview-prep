from typing import List

class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     '''
    #     DFS Iterative
    #     m is the number of rows and n is the number of cols
    #     Time Complexity: O(m*n)
    #     Space Complexity: O(m*n)
    #     '''
    #     islands = 0
    #     for i in range(len(grid)):
    #         for j in range(len(grid[0])):
    #             if grid[i][j] == '1':
    #                 islands += 1
    #                 stack = [(i, j)]
    #                 while stack:
    #                     row, col = stack.pop()
    #                     if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == '1':
    #                         grid[row][col] = '0'
    #                         stack += [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

    #     return islands
    
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        DFS Recursive
        m is the number of rows and n is the number of cols
        Time Complexity: O(m*n)
        Space Compleixty: O(m*n)
        '''
        def numIslands(i, j, grid=grid):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = '0'
                numIslands(i - 1, j)
                numIslands(i + 1, j)
                numIslands(i, j - 1)
                numIslands(i, j + 1)

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands += 1
                    numIslands(i, j)

        return islands


def main():
    s = Solution()

    grid = [
        ['1', '1', '1', '1,', '0'],
        ['1', '1', '0', '1,', '0'],
        ['1', '1', '0', '0,', '0'],
        ['0', '0', '0', '0,', '0'],
    ]
    print(s.numIslands(grid))

    grid = [
        ['1', '1', '0', '0,', '0'],
        ['1', '1', '0', '0,', '0'],
        ['0', '0', '1', '0,', '0'],
        ['0', '0', '0', '1,', '1'],
    ]
    print(s.numIslands(grid))

if __name__ == '__main__':
    main()