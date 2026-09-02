class StringOperations:
    def reverse(self, s):
        return s[::-1]

    def count_vowels(self, s):
        return sum(1 for ch in s.lower() if ch in 'aeiou')

    def is_palindrome(self, s):
        clean = ''.join(ch.lower() for ch in s if ch.isalnum())
        return clean == clean[::-1]

if __name__ == '__main__':
    so = StringOperations()
    text = 'Madam'
    print('Reverse:', so.reverse(text))
    print('Vowels:', so.count_vowels(text))
    print('Palindrome:', so.is_palindrome(text))
