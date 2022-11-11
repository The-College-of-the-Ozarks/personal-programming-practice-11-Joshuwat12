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

p1 = input_Point()
c1 = input_Circle()

print(p1)
print(c1)