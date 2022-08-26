import time


SYMBOLS = ['|||', '///', '---', '\\\\\\']


def spiner(sec):
    for _ in range(sec):
        for spin in SYMBOLS:
            time.sleep(0.25)
            print('\r', spin, end='')


timer = int(input('How long? (sec): '))
spiner(timer)
