import os
import sys


def solution(path):
    if len(os.listdir(path)) == 0:
        raise FileExistsError("Add the initial data files")
    result = [0 in range(16)]
    for filename in os.listdir(path):
        with open(path + filename) as file:
            result = [result[i] + j for i, j in
                      zip(range(16), [float(line.rstrip()[:-2]) for line in file])]
    return result.index(max(result)) + 1


if __name__ == '__main__':
    try:
        print(solution(sys.argv[1]))
    except ValueError:
        print("The initial files are empty")
