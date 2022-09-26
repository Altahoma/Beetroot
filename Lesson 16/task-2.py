import calendar


class Mathematician:
    @staticmethod
    def square_nums(lst):
        return [num**2 for num in lst]

    @staticmethod
    def remove_positives(lst):
        return [num for num in lst if num < 0]

    @staticmethod
    def filter_leaps(lst):
        return [year for year in lst if calendar.isleap(year)]


m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
