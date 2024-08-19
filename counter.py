class Counter(object):
    def __init__(self, start=0):
        self.count = start

    def add(self, amount=1):
        self.count += amount
        return self.count

    def subtract(self, amount=1):
        self.count -= amount
        return self.count


def main():
    a = Counter(5)
    print(a.add(5))
    print(a.subtract(2))
    test_counter()


def test_counter():
    counter_a = Counter()
    counter_a.add()
    counter_a.add()
    counter_a.add()
    counter_a.add()
    assert counter_a.count == 4, "Counter A should be 4"
    counter_a.subtract()
    counter_a.subtract()
    counter_a.subtract()
    assert counter_a.count == 1, "Counter A should be 1"
    counter_a.subtract()
    counter_a.subtract()
    counter_a.subtract()
    counter_a.subtract()
    counter_a.subtract()
    assert counter_a.count == -4, "Counter A should be -4"

    print("All tests have been passed!")


if __name__ == '__main__':
    main()
