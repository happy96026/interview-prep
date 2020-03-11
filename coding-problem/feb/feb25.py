# class Solution:
#   def word_search(self, matrix, word):
#     for i in range(len(matrix)):
#       k = 0
#       for j in range(len(matrix[0])):
#         if j + len(word) - 1 - k >= len(matrix[0]):
#           break
#         k = k + 1 if matrix[i][j] == word[k] else 0
#         if k >= len(word):
#           return True

#     for j in range(len(matrix[0])):
#       k = 0
#       for i in range(len(matrix)):
#         if i + len(word) - 1 - k >= len(matrix):
#           break
#         k = k + 1 if matrix[i][j] == word[k] else 0
#         if k >= len(word):
#           return True

#       return False

class Solution:
  def word_search(self, matrix, word):
    start = []

    for i in range(len(matrix)):
      k = 0
      for j in range(len(matrix[0])):
        k = k + 1 if matrix[i][j] == word[k] else 0
        if k >= len(word):
          return True
        elif matrix[i][j] == word[0] and i + len(word) - 1 < len(matrix):
          start.append((i, j))
    
    for start_row, j in start:
      k = 0
      for i in range(start_row, start_row + len(word)):
        if matrix[i][j] != word[k]:
          break
        k += 1

      if k == len(word):
        return True

    return False


def main():
  s = Solution()
  matrix = [
    ['F', 'O', 'A', 'M'],
    ['O', 'B', 'F', 'P'],
    ['A', 'N', 'O', 'B'],
    ['F', 'A', 'S', 'K'],
  ]
  print(s.word_search(matrix, 'BFP'))

if __name__ == '__main__':
  main()