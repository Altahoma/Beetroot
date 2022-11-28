import threading


class Counter(threading.Thread):
    counter = 0
    rounds = 100000

    def run(self):
        for _ in range(Counter.rounds):
            Counter.counter += 1


t1 = Counter()
t2 = Counter()

t1.start()
t2.start()

print(f'Before waiting: {Counter.counter}')

t1.join()
t2.join()

print(f'After waiting: {Counter.counter}')
