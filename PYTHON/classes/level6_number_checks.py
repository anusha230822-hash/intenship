class Number:
    def __init__(self, n):
        self.n = n

    def is_even(self):
        return self.n % 2 == 0

    def is_odd(self):
        return self.n % 2 != 0

    def is_prime(self):
        if self.n < 2:
            return False
        if self.n == 2:
            return True
        if self.n % 2 == 0:
            return False
        i = 3
        while i * i <= self.n:
            if self.n % i == 0:
                return False
            i += 2
        return True

    def is_palindrome(self):
        s = str(self.n)
        return s == s[::-1]

if __name__ == '__main__':
    num = Number(121)
    print('Even:', num.is_even())
    print('Odd:', num.is_odd())
    print('Prime:', num.is_prime())
    print('Palindrome:', num.is_palindrome())
