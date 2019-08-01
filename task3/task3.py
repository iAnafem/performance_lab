import os
import sys


def solution(path):
    if len(os.listdir(path)) == 0:
        raise FileExistsError("Add initial data files")
    result = [0 for x in range(16)]
    for filename in os.listdir(path):
        if filename.endswith('.txt'):
            with open(path + filename) as file:
                result = [i + j for i, j in zip(result, (float(line.rstrip()[:-2]) for line in file if line != '\n'))]
    return result.index(max(result)) + 1


if __name__ == '__main__':
    try:
        print(solution(sys.argv[1]))
    except ValueError:
        print("Initial data files are empty")
