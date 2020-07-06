class Solution:
    def myAtoi(self, str: str) -> int:
        states = {
            'start': { 
                'whitespace': 'start', 
                'plus_minus': 'plus_minus', 
                'number': 'number', 
                'char': 'exit'
            },
            'plus_minus': { 
                'whitespace': 'exit', 
                'plus_minus': 'exit', 
                'number': 'number', 
                'char': 'exit'
            },
            'number': { 
                'whitespace': 'ok',
                'plus_minus': 'ok',
                'number': 'number',
                'char': 'ok',
            },
            'ok': {},
            'exit': {}
        }
        BOUND = 2 ** 31 // 10
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1

        state = 'start'
        isMinus = False
        integer = 0

        for c in str:
            if c == ' ':
                transition = 'whitespace'
            elif c in ('+', '-'):
                transition = 'plus_minus'
            elif c.isdigit():
                transition = 'number'
            else:
                transition = 'char'

            state = states[state][transition]

            if state == 'start':
                pass

            elif state == 'plus_minus':
                if c == '-':
                    isMinus = True

            elif state == 'number':
                n = int(c)
                if (integer > BOUND) or (integer == BOUND and n > (8 if isMinus else 7)):
                    return INT_MIN if isMinus else INT_MAX

                integer *= 10
                integer += n

            elif state == 'ok':
                break

            else:
                return 0

        return integer * (-1 if isMinus else 1)


def main():
    s = Solution()
    print(s.myAtoi('42'))
    print(s.myAtoi('-42'))
    print(s.myAtoi('4193 with words'))
    print(s.myAtoi('words and 987'))
    print(s.myAtoi('-91283472332'))

if __name__ == '__main__':
    main()
