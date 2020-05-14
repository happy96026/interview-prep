class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        currWord = ''

        for c in path + '/':
            if c == '/':
                if currWord == '..':
                    if stack: stack.pop()
                elif currWord and currWord != '.':
                    stack.append(currWord)
                
                currWord = ''
            else:
                currWord += c

        return '/' + '/'.join(stack)

def main():
    s = Solution()
    print(s.simplifyPath('/Users/Joma/Documents/../Desktop/./../'))
    print(s.simplifyPath('/../'))
    print(s.simplifyPath('/home//foo/'))
    print(s.simplifyPath('/a/./b/../../c/'))
    print(s.simplifyPath('/a/./b/../../c/'))
    print(s.simplifyPath('/a//b////c/d//././/..'))

if __name__ == '__main__':
    main()