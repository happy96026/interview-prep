from collections import deque

# BFS Solution
# class Solution:
#     def pushDominoes(self, dominoes):
#         q = deque()
#         dominoes = list(dominoes)
#         time_list = [0] * len(dominoes)

#         for i, d in enumerate(dominoes):
#             if d != '.':
#                 q.append(i)

#         while q:
#             i = q.popleft()
#             if dominoes[i] == 'R' and i + 1 < len(dominoes) and dominoes[i + 1] == '.':
#                 dominoes[i + 1] = 'R'
#                 time_list[i + 1] = time_list[i] + 1
#                 q.append(i + 1)
#             elif dominoes[i] == 'L' and i - 1 >= 0:
#                 if dominoes[i - 1] == '.':
#                     dominoes[i - 1] = 'L'
#                     time_list[i - 1] = time_list[i] + 1
#                     q.append(i - 1)
#                 elif dominoes[i - 1] == 'R' and time_list[i - 1] == time_list[i] + 1:
#                     dominoes[i - 1] = '.'

#         return ''.join(dominoes)

# Calculate Force Solution
# class Solution:
#     def pushDominoes(self, dominoes):
#         forces = [0] * len(dominoes)

#         force = 0
#         for i in range(len(dominoes)):
#             if dominoes[i] == 'R':
#                 force = len(dominoes)
#             elif dominoes[i] == 'L':
#                 force = 0
#             elif force > 0:
#                 force -= 1
#             forces[i] += force

#         force = 0
#         for i in range(len(dominoes) - 1, -1, -1):
#             if dominoes[i] == 'L':
#                 force = -len(dominoes)
#             elif dominoes[i] == 'R':
#                 force = 0
#             elif force < 0:
#                 force += 1
#             forces[i] += force
        
#         return ''.join(['R' if force > 0 else 'L' if force < 0 else '.' for force in forces])

# Ajdacent String Solution
class Solution:
    def pushDominoes(self, dominoes):
        pass


def main():
    print(Solution().pushDominoes('.L.R...LR..L..'))

if __name__ == '__main__':
    main()