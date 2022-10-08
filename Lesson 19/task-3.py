from copy import copy


class InRange:
    def __init__(self, start, end, step=1):
        if step == 0:
            raise ValueError
        self.start = start
        self.end = end
        self.step = step
        self.current_num = start

    def __iter__(self):
        return copy(self)

    def __next__(self):
        if self.step > 0:
            if self.current_num < self.end:
                num = self.current_num
                self.current_num += self.step
                return num
        if self.step < 0:
            if self.current_num > self.end:
                num = self.current_num
                self.current_num += self.step
                return num
        raise StopIteration

    def __len__(self):
        length = 0
        for _ in self:
            length += 1
        return length

    def get_item_by_key(self, key):
        index = 0
        for element in self:
            if index == key:
                return element
            index += 1

    def __getitem__(self, key):
        if isinstance(key, slice):
            start, stop, step = key.indices(len(self))
            return [self[i] for i in InRange(start, stop, step)]
        elif isinstance(key, int):
            if key < 0:
                key += len(self)
            elif key >= len(self):
                raise IndexError('Range object index out of range')
            return self.get_item_by_key(key)
        else:
            raise TypeError(f'Invalid argument type: {type(key)}')


if __name__ == '__main__':
    my_iterable = InRange(-10, 10)
    python_iterable = range(-10, 10)

    for number in InRange(0, 5):
        print(number)

    assert list(my_iterable) == list(python_iterable)
    assert len(my_iterable) == len(python_iterable)
    assert my_iterable[4] == python_iterable[4]
    assert my_iterable[-2] == python_iterable[-2]
    assert list(my_iterable[5:10:2]) == list(python_iterable[5:10:2])
    assert list(InRange(0, 10, 2)) == list(range(0, 10, 2))
