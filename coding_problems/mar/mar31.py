class Solution:
    # def minRemoveToMakeValid(self, s: str) -> str:
    #     '''
    #     Stack
    #     Time Complexity: O(n)
    #     Space Compleixty: O(n)
    #     '''
    #     s = [c for c in s]
    #     stack = []
    #     for i, c in enumerate(s):
    #         if c == '(':
    #             stack.append(i)
    #         elif c == ')':
    #             if stack:
    #                 stack.pop()
    #             else:
    #                 s[i] = ''
               
    #     for i in stack:
    #         s[i] = ''

    #     return ''.join(s)

    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        Two-pass
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        s = [c for c in s]

        counter = 0
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                counter += 1
            elif c == ')':
                if counter == 0:
                    s[i] = ''
                else:
                    counter -= 1

        counter = 0
        for i in reversed(range(len(s))):
            c = s[i]
            if c == ')':
                counter += 1
            elif c == '(':
                if counter == 0:
                    s[i] = ''
                else:
                    counter -= 1

        return ''.join(s)


def main():
    s = Solution()
    print(s.minRemoveToMakeValid('lee(t(c)o)de)'))
    print(s.minRemoveToMakeValid('a)b(c)d'))
    print(s.minRemoveToMakeValid('))(('))
    print(s.minRemoveToMakeValid('(a(b(c)d)'))

if __name__ == '__main__':
    main()