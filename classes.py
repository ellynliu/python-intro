import math

# Class to represent a point
# distance_to method is used to calculate the distance between two points
class Point:
    def __init__(self, x_val, y_val):
        self.x = x_val
        self.y = y_val
    def distance_to(self, point2):
        return math.sqrt((point2.x - self.x) ** 2 + (point2.y - self.y) ** 2)

point1 = Point(5, 3)
point2 = Point(1, 2)
print(point1.x)
print(point1.y)
# There are two ways to call a method, but the first method below is more frequently used
print(point1.distance_to(point2))
print(Point.distance_to(point1, point2))

# Class to represent an RGB color
class Color:
    def __init__(self, red, green, blue):
        self.r = red
        self.g = green
        self.b = blue

    # The luminance roughly represents the brightness of the pixel
    def luminance(self):
        return 0.2126*self.r + 0.7152*self.g + 0.0722*self.b

    # Return False if RGB values go out of bounds  
    def verify_rgb(self):
        return 0 <= self.r <= 255 and 0 <= self.g <= 255 and 0 <= self.b <= 255

c1 = Color(10, 15, 50)
print(c1.luminance())
print(Color.luminance(c1))
print(c1.verify_rgb())
