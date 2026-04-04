class Vector2D:
    """A 2D vector with Cartesian coordinates."""

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        """Human-readable string representation defined."""
        return '{:d}i + {:d}j'.format(self.x, self.y)

    def __repr__(self):
        """Unambiguous string representation."""
        return repr((self.x, self.y))

    def __add__(self, other):
        """Vector addition."""
        return Vector2D(self.x + other.x, self.y + other.y)

    def __matmul__(self, other):
        try:
            if not isinstance(other, Vector2D):
                raise TypeError
            return self.x * other.x + self.y * other.y
        except TypeError:
            print('Dot product of two Vector2D objects only')

    def __mul__(self, other):
        try:
            if isinstance(other, Vector2D):
                raise NotImplementedError
            return Vector2D(self.x * other, self.y * other)
        except NotImplementedError:
            print('Multiply a scalar only')

    def __rmul__(self, other):
        return self.__mul__(other)


if __name__ == '__main__':
    v1 = Vector2D(2, 3)
    v2 = Vector2D(4, 5)
    print(v1 @ v2)      
    print(v1 @ 1)       
    print(v1 * 2)       
    print(2 * v2)      
    print(v1 * v2)      