import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))


def intersect_rectangle(R1, R2):
    # TODO - you fill in here.
    """
    DATE : 29 May
    APPROCH : This problem is solved by first considering the case where we find weather the Recatange make any
    intersection with the other Recatangle after that the co-ordinate of the intersecting rectangle found by
    taking a difference from the co-ordinate.

    THINGS TO DO : Draw diagram, look for the corner case.

    BIG-O : It is a constant time algorithms as it only checks the co-ordinates of the recatangle

    :param R1:
    :param R2:
    :return:
    """

    def is_intersect(R1, R2):
        return  (R1.x+ R1.width >= R2.x and R1.y + R1.height >= R2.y
                 and R1.x <= R2.x + R2.width and R1.y <= R2.y + R2.height)

    if not is_intersect(R1, R2):
        return Rectangle(0, 0, -1, -1)
    if is_intersect(R1, R2):
        return Rectangle(max(R1.x, R2.x),
                         max(R1.y, R2.y),
                         min(R1.x + R1.width, R2.x + R2.width) - max(R1.x, R2.x),
                         min(R1.y + R1.height, R2.y + R2.height) - max(R1.y, R2.y))




def intersect_rectangle_wrapper(R1, R2):
    return intersect_rectangle(Rectangle(*R1), Rectangle(*R2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "rectangle_intersection.py",
            'rectangle_intersection.tsv',
            intersect_rectangle_wrapper,
            res_printer=res_printer))
