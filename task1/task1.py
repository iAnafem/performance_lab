import sys
import numpy


def solution(test_file: str):
    with open(test_file) as file:
        array = [int(line) for line in file]
        return (
            numpy.percentile(array, 90),
            numpy.median(array),
            numpy.max(array),
            numpy.min(array),
            numpy.mean(array),
        )


if __name__ == '__main__':
    try:
        for number in solution(sys.argv[1]):
            print('{:0.2f}'.format(number))

        assert list(solution(sys.argv[1])) == [8.20, 5.00, 10.00, 0.00, 4.50]

    except (FileNotFoundError, TypeError):
        print('No such a file or directory')

