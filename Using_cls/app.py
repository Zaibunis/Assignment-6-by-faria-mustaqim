class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
    def show_count(cls):
        print(f"Objects created: {cls.count}")

a = Counter()
b = Counter()
c = Counter()
Counter.show_count(cls=Counter)
