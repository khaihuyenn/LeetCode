class Solution(object):
    def reverseWords(self, s):
        # Split the string into words
        # "hello wordd" --> ['hello', 'world']
        words = s.split()
        # Reverse the order of words
        # ['hello', 'world'] --> ['world', 'hello']
        reversed_words = words[::-1]
        # Join the reversed words with spaces
        # ['world', 'hello'] --> "world hello"
        reversed_string = ' '.join(reversed_words)

        return reversed_string
        