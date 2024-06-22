class Solution(object):
    def reverseVowels(self, s):
        vowels = set('aeiouAEIOU')
        # Convert the string into character array
        char = list(s)
        # Initialize two pointers
        left, right = 0, len(char) - 1

        while left < right:
            while left < right and char[left] not in vowels:
                left += 1
            while left < right and char[right] not in vowels:
                right -= 1
            if left < right:
                char[left], char[right] = char[right], char[left]
                left += 1
                right -= 1
        # Join the reversed vowels        
        reverse_vowels = ''.join(char)
        return reverse_vowels
        