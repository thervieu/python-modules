class Vector(object):
    def __init__(self, *args):
        """ Create a vector, example: v = Vector(1,2) """
        self.values = []
        if len(args) == 0:
            raise ValueError("Vector: can't initialize with no argument")
        elif len(args) == 1 and isinstance(args[0], int):
            for i in range(args[0]):
                self.values.append(i)
        elif len(args) == 1 and isinstance(args[0], int) and isinstance(args[1], int):
            for i in range(args[0], argv[1]):
                self.values.append(i)
        else:
            for a in args[0]:
                self.values.append(a)
        if isinstance(self.values[0], float):
            self.shape = (1, len(self.values))
        else:
            self.shape = (len(self.values), 1)

    def T(self):
        transpose = []

        if isinstance(self.values[0], float):
            for a in self.values:
                transpose.append([a, ])
        else:
            for a in self.values:
                transpose.append(a[0])
        return self.__class__(*(transpose, ))

    def dot(self, vector):
        """ Returns the dot product (dot product) of self and another vector
        """
        if not isinstance(vector, Vector):
            raise TypeError('Vector: dot: requires two vectors')
        if self.shape != vector.shape:
            raise ValueError('Vector: dot: different shape')
        if isinstance(self.values[0], float):
            return sum(a * b for a, b in zip(self.values, vector.values))
        else:
            return sum(a[0] * b[0] for a, b in zip(self.values, vector.values))

    def __add__(self, other):
        """ Returns the vector addition of self and other """
        added = []
        if isinstance(self.values[0], float):
            if isinstance(other, Vector):
                if self.shape != other.shape:
                    raise ValueError('Vector: add: different shape')
                for a, b in zip(self.values, other.values):
                    added.append(a + b)
            elif isinstance(other, (int, float)):
                for a in self.values:
                    added.append(a + other)
            else:
                raise TypeError("Vector: add: type {} not supported".format(
                    type(other)))
        else:
            if isinstance(other, Vector):
                if self.shape != other.shape:
                    raise ValueError('Vector: add: different shape')
                for a, b in zip(self.values, other.values):
                    added.append([a[0] + b[0]])
            elif isinstance(other, (int, float)):
                for a in self.values:
                    added.append([a[0] + other])
            else:
                raise TypeError("Vector: add: type {} not supported".format(
                    type(other)))

        return self.__class__(*(added, ))

    def __radd__(self, other):
        """ Called if 4 + self for instance """
        return self.__add__(other)

    def __sub__(self, other):
        """ Returns the vector substraction of self and other """
        subbed = []
        if isinstance(self.values[0], float):
            if isinstance(other, Vector):
                if self.shape != other.shape:
                    raise ValueError('Vector: add: different shape')
                for a, b in zip(self.values, other.values):
                    subbed.append(a - b)
            elif isinstance(other, (int, float)):
                for a in self.values:
                    subbed.append(a - other)
            else:
                raise TypeError("Vector: substraction: type {} not supported".format(
                    type(other)))
        else:
            if isinstance(other, Vector):
                if self.shape != other.shape:
                    raise ValueError('Vector: add: different shape')
                for a, b in zip(self.values, other.values):
                    subbed.append([a[0] - b[0]])
            elif isinstance(other, (int, float)):
                for a in self.values:
                    subbed.append([a[0] - other])
            else:
                raise TypeError("Vector: substraction: type {} not supported".format(
                    type(other)))

        return self.__class__(*(subbed, ))

    def __rsub__(self, other):
        """ Called if 4 + self for instance """
        return self.__sub__(other)

    def __mul__(self, other):
        """ Returns the vector multiplication of self and other """
        product = []
        if isinstance(self.values[0], float):
            if isinstance(other, (int, float)):
                for a in self.values:
                    product.append(a * other)
            else:
                raise TypeError("Vector: mul: type {} not supported".format(
                    type(other)))
        else:
            if isinstance(other, (int, float)):
                for a in self.values:
                    product.append([a[0] * other])
            else:
                raise TypeError("Vector: mul: type {} not supported".format(
                    type(other)))

        return self.__class__(*(product, ))

    def __rmul__(self, other):
        """ Called if 4 + self for instance """
        return self.__mul__(other)

    def __truediv__(self, other):
        """ Returns the vector division of self and other """
        div = []
        if isinstance(self.values[0], float):
            if isinstance(other, (int, float)):
                for a in self.values:
                    div.append(a / other)
            else:
                raise TypeError("Vector: div: type {} not supported".format(
                    type(other)))
        else:
            if isinstance(other, (int, float)):
                for a in self.values:
                    div.append([a[0] / other])
            else:
                raise TypeError("Vector: div: type {} not supported".format(
                    type(other)))

        return self.__class__(*(div, ))

    def __rtruediv__(self, other):
        """ Called if 4 + self for instance """
        if isinstance(self, Vector):
            raise TypeError("Vector: div: type {} not supported".format(
                type(self)))

        return self.__truediv__(other)

    def __iter__(self):
        return self.values.__iter__()

    def __str__(self):
        return str(self.values)

    def __repr__(self):
        return str(self.values)