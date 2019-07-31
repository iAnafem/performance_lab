import sys
import matplotlib.path as mpl_path
import numpy


class Point:
    def __init__(self, _list):
        self.coordinates = _list
        self.x = _list[0]
        self.y = _list[1]


class Quadrilateral:
    def __init__(self, edges):
        self.quadrilateral = mpl_path.Path(numpy.array(edges))
        self.points = list()
        self.max_x = max([i[0] for i in edges])
        self.min_x = min([i[0] for i in edges])
        self.max_y = max([i[0] for i in edges])
        self.min_y = min([i[0] for i in edges])
        for edge in edges:
            self.points.append(Point(edge))
        self.left_bottom = self.points[0]
        self.left_top = self.points[1]
        self.right_top = self.points[2]
        self.right_bottom = self.points[3]

    def point_on_edge(self, point: Point) -> bool:
        for edge in self.points:
            if point.coordinates == edge.coordinates:
                return True

    def point_on_side(self, point: Point) -> bool:
        """
        I know that this is crazy, but I do not know how to check in another way
        whether the points on the sides of the quadrilateral lie ...
        """
        if (
                (point.x - self.left_bottom.x) *
                (self.right_bottom.y - self.left_bottom.y) -
                (self.right_bottom.x - self.left_bottom.x) *
                (point.y - self.left_bottom.y)
        ) == 0 and self.left_bottom.x <= point.x <= self.right_bottom.x or (
                (point.x - self.left_top.x) *
                (self.right_top.y - self.left_top.y) -
                (self.right_top.x - self.left_top.x) *
                (point.y - self.left_top.y)
        ) == 0 and self.left_top.x <= point.x <= self.right_top.x or (
                (point.x - self.right_bottom.x) *
                (self.right_top.y - self.right_bottom.y) -
                (self.right_top.x - self.right_bottom.x) *
                (point.y - self.right_bottom.y)
        ) == 0 and self.left_bottom.y <= point.y <= self.left_top.y or (
                (point.x - self.left_bottom.x) *
                (self.left_top.y - self.left_bottom.y) -
                (self.left_top.x - self.left_bottom.x) *
                (point.y - self.left_bottom.y)
        ) == 0 and self.right_bottom.y <= point.y <= self.right_top.y:
            return True

    def point_inside(self, point: Point) -> bool:
        return self.quadrilateral.contains_point(point.coordinates, radius=0.1)


def get_points(test_file: str) -> list:
    with open(test_file) as file:
        return [[float(i[0]), float(i[1])] for line in file for i in [line.rstrip()[:-2].split(' ')]]


def solution(test_file1, test_file2):
    quadrilateral = Quadrilateral(get_points(test_file1))
    points = get_points(test_file2)
    result = []
    for point in points:
        _point = Point(point)
        if quadrilateral.point_on_edge(_point):
            result.append(0)
        elif not quadrilateral.point_on_edge(_point) and quadrilateral.point_on_side(_point):
            result.append(1)
        elif quadrilateral.point_inside(_point):
            result.append(2)
        else:
            result.append(3)
    return result


if __name__ == '__main__':
    for res in solution(sys.argv[1], sys.argv[2]):
        print(res)

    assert solution(sys.argv[1], sys.argv[2]) == [2, 3, 1, 0, 3, 1, 1, 1, 1, 3]



