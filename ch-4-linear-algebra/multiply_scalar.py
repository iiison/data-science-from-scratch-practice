from typing import List

Vector = List[float]

def mul_scalar(c: float, v: Vector) -> Vector:
    """Multiplies the vetor - v with Scalar value c"""

    assert v
    return [c * v_i for v_i in v]


assert mul_scalar(5, [1, 2, 3, 4]) == [5, 10, 15, 20]
