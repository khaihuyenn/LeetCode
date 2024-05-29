class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        mapping = { 
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        result = []
        def backtrack(combination, digit):
            if not digit:
                result.append(combination)
            else:
                for letter in mapping[digit[0]]:
                    backtrack(combination + letter, digit[1:])
        backtrack("", digits)
        return result