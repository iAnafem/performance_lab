from datetime import datetime as dt
import sys


class Interval:
    def __init__(self, interval: list):
        self.start = dt.strptime(interval[0], "%H:%M")
        self.finish = dt.strptime(interval[1], "%H:%M")


def get_intervals(test_file: str) -> list:
    with open(test_file) as file:
        return [[i[0], i[1]] for line in file for i in [line.rstrip()[:-2].split(' ')] if line != '\n']


def solution(initial_data: list):
    intervals = sorted([Interval(i) for i in initial_data], key=lambda x: x.finish)
    result = [[intervals[0].start, intervals[0].finish, 0]]
    max_count = 0
    for index, interval in enumerate(intervals):
        min_time = interval.start
        temp_count = 0
        i = index
        while i < len(intervals):
            if interval.finish > intervals[i].start:
                if min_time < intervals[i].start:
                    min_time = intervals[i].start
                temp_count += 1
            i += 1
        if max_count == temp_count and min_time <= result[-1][1]:
            result[-1][1] = interval.finish
        elif max_count == temp_count and min_time > result[-1][1]:
            result.append([min_time, interval.finish, temp_count])
        elif max_count < temp_count:
            max_count = temp_count
            result[-1] = [min_time, interval.finish, temp_count]
    return result


if __name__ == '__main__':
    for res in solution(get_intervals(sys.argv[1])):
        print(f'{res[0].hour}:{res[0].minute:02d} {res[1].hour}:{res[1].minute:02d}\\n')




