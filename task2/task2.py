import sys
import matplotlib.path as mpl_path
import numpy


class Point:
    def __init__(self, _list):
        self.coordinates = _list
        self.x = _list[0]
        self.y = _list[1]


class Rectangle:
    def __init__(self, edges):
        self.rectangle = mpl_path.Path(numpy.array(edges))
        self.points = list()
        for edge in edges:
            self.points.append(Point(edge))
        self.left_bottom = self.points[0]
        self.right_bottom = self.points[1]
        self.right_top = self.points[2]
        self.left_top = self.points[3]

    def point_on_edge(self, point: Point) -> bool:
        for edge in self.points:
            if point.coordinates == edge.coordinates:
                return True

    def point_on_side(self, point: Point) -> bool:
        if (
                (point.x - self.left_bottom.x) *
                (self.right_bottom.y - self.left_bottom.y) -
                (self.right_bottom.x - self.left_bottom.x) *
                (point.y - self.left_bottom.y)
        ) == 0 or (
                (point.x - self.left_top.x) *
                (self.right_top.y - self.left_top.y) -
                (self.right_top.x - self.left_top.x) *
                (point.y - self.left_top.y)
        ) == 0 or (
                (point.x - self.right_bottom.x) *
                (self.right_top.y - self.right_bottom.y) -
                (self.right_top.x - self.right_bottom.x) *
                (point.y - self.right_bottom.y)
        ) == 0 or (
                (point.x - self.left_bottom.x) *
                (self.left_top.y - self.left_top.y) -
                (self.left_top.x - self.left_bottom.x) *
                (point.y - self.left_bottom.y)
        ) == 0:
            return True

    def point_inside(self, point: Point) -> bool:
        return self.rectangle.contains_point(point.coordinates)


def get_points(test_file: str) -> list:
    with open(test_file) as file:
        return [[float(i[0]), float(i[1])] for line in file for i in [line.rstrip()[:-2].split(' ')]]


def solution(test_file1, test_file2):
    rectangle = Rectangle(get_points(test_file1))
    print(rectangle.rectangle)
    points = get_points(test_file2)
    result = []
    for point in points:
        _point = Point(point)
        if rectangle.point_on_edge(_point):
            print(_point.coordinates)
            print(0)
            result.append(0)
        elif rectangle.point_on_side(_point):
            print(_point.coordinates)
            print(1)
            result.append(1)
        elif rectangle.point_inside(_point):
            print(_point.coordinates)
            print(2)
            result.append(2)
        else:
            print(_point.coordinates)
            print(3)
            result.append(3)
    return result


if __name__ == '__main__':
    print(get_points(sys.argv[1]))
    print(get_points(sys.argv[2]))
    for res in solution(sys.argv[1], sys.argv[2]):
        continue

    # assert solution(sys.argv[1], sys.argv[2]) == [2, 3, 1, 0, 3]



