import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return math.sqrt(sum(coordinates_squared))

    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scaler(1./magnitude)
        
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')


    def plus(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)


    def minus(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)


    def times_scaler(self, c):
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(new_coordinates)

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates


v = Vector([8.218,-9.341])
w = Vector([-1.129,2.111])
print ('Plus ',v.plus(w))

v = Vector([7.119,8.215])
w = Vector([-8.223,0.878])
print ('Minus ',v.minus(w))

v = Vector([1.671,-1.012,-0.318])
c = 7.41
print ('Scaler ',v.times_scaler(c))

v = Vector([-0.221,7.437])
print ('Magnitude ',v.magnitude())

v = Vector([8.813,-1.331,-6.247])
print ('Magnitude ',v.magnitude())

v = Vector([5.581,-2.136])
print ('Magnitude ',v.magnitude())

v = Vector([5.581,-2.136])
print ('Normalized ',v.normalized())

v = Vector([1.996,3.108,-4.554])
print ('Normalized ',v.normalized())