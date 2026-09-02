class Temperature:
    def c_to_f(self, c):
        return (c * 9/5) + 32

    def f_to_c(self, f):
        return (f - 32) * 5/9

if __name__ == '__main__':
    t = Temperature()
    print('0C ->', t.c_to_f(0))
    print('32F ->', t.f_to_c(32))
