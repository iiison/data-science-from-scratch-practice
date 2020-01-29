from typing import List

Vector = List[float]

def add_multiple_vectors(vectors: List[Vector]) -> Vector:
    """Sums more than 2 vectors"""

    #Checks if `vectors` has values
    assert vectors

    num_el = len(vectors[0])

    # Check if all elements are of same length
    assert all(len(v) == num_el for v in vectors)

    return [sum(vector[i] for vector in vectors) for i in range(num_el)]


TEST_VECTORS = [[1, 2], [3, 4], [5, 6], [7, 8]]

assert add_multiple_vectors(TEST_VECTORS) == [16, 20]
