from typing import List

Vector = List[float]

def add_vector(v: Vector, w: Vector) -> Vector:
    """Adds Vectors"""

    assert len(v) == len(w)

    return [v_i + w_i for v_i, w_i in zip(v, w)]

assert add_vector([1, 2, 3], [4, 5, 6]) == [5, 7, 9]


def subtract_vector(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w)

    return [v_i - w_i for v_i, w_i in zip(v, w)]

assert subtract_vector([4, 5, 6], [1, 2, 3]) == [3, 3, 3]
