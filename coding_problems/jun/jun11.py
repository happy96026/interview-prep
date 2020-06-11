class Solution:
    def flattenDictionary(self, d):
        result = {}
        stack = [(d, '')]
        while stack:
            x, prefix = stack.pop()
            if isinstance(x, dict):
                for k in reversed(x):
                    stack.append((x[k], prefix + ('.' if prefix else '') + k))
            else:
                result[prefix] = x

        return result


def main():
    s = Solution()
    print(s.flattenDictionary({ 'a': 1, 'b': { 'c': 2, 'd': { 'e': 3 } }, 'c': { 'a': 4, 'b': 2 } }))
    print(s.flattenDictionary({}))
    print(s.flattenDictionary({ 'a': 1 }))

if __name__ == '__main__':
    main()
