import math

# Points contain x- and y-coordinate
# Instantiated by Point(x, y)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point: ({self.x},{self.y})"

# Circles contain a center Point and radius
# Instantiate by Circle(x, y, r)
#          or by Circle(p, r) with p a Point
class Circle:
    def __init__(self, x, y, r = None):
        if r is None:
            self.center = x
            self.r = y
        else:
            self.center = Point(x, y)
            self.r = r
    
    def __repr__(self):
        return f"Circle: ({self.center.x},{self.center.y}), r={self.r}"

def input_Point():
    raw_point = input("Input the point in the form (x,y)\n")
    raw_point = raw_point.replace('(','')
    raw_point = raw_point.replace(')','')
    raw_point = raw_point.replace(' ','')
    point = raw_point.split(',')
    return Point(float(point[0]), float(point[1]))

def input_Circle():
    print("Input the center of the circle:")
    center = input_Point()
    r = input("Input the radius\n")
    return Circle(center, float(r))

def distance(point1, point2):
  return ((point1.x - point2.x)**2 + (point1.y - point2.y)**2) ** 0.5

def slope(point1, point2):
  return (point1.y - point2.y) / (point1.x - point2.x)

def circumference(circle):
  return math.pi * circle.r * 2

def area(circle):
  return math.pi * circle.r ** 2

def in_circle(point, circle):
  return distance(point, circle.center) <= circle.r

print("For Point 1:")
p1 = input_Point()
print("For Point 2:")
p2 = input_Point()
c1 = input_Circle()

print(p1)
print(p2)
print(c1)

# print(distance(p1, p2))
# print(slope(p1, p2))
# print(circumference(c1))
# print(area(c1))
print(in_circle(p1, c1))