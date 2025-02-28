import math
class Vector:
    def __init__(self, *args):


        if not all(isinstance(x,(int,float)) for x in args):
            print("All vector components must be numbers.")

        self.components = tuple(args)

    def __repr__(self):
        return f"{self.components}"
    def __add__(self, vector2):
        if not all(isinstance(vector2,Vector) or len(self.components)!= len(vector2)):
            raise ValueError("They are not equal in length")

        result = tuple(a+b for a,b in zip(self.components, vector2))
        return Vector(*result)
    def __sub__(self, vector2):
        if not all(isinstance(vector2,Vector) or len(self.components)!= len(vector2)):
            raise ValueError("They are not equal in length")
        result = tuple(a - b for a, b in zip(self.components, vector2))
        return Vector(*result)

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise ValueError("Scalar must be a number.")

        result = tuple(a * scalar for a in self.components)
        return Vector(*result)

    def dot(self, other):
        if not isinstance(other, Vector) or len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for dot product.")

        return sum(a * b for a, b in zip(self.components, other.components))

    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")

        return Vector(*(a / mag for a in self.components))


v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1)
print(v1 + v2)
print(v1 - v2)
print(v1 * 2)
print(v1.dot(v2))
print(v1.magnitude())
print(v1.normalize())