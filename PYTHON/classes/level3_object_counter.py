class CounterExample:
    count = 0

    def __init__(self):
        CounterExample.count += 1

if __name__ == '__main__':
    o1 = CounterExample()
    o2 = CounterExample()
    o3 = CounterExample()
    print('Total objects:', CounterExample.count)
