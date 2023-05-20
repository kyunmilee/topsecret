class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def set_dimension(self, length, width):
        self.__length = length
        self.__width = width

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)

    def print(self):
        print("Rectangle 생성")
        print("Length = {}, Width = {}, Area = {}, Perimeter = {}".format(self.__length, self.__width, self.area(), self.perimeter()))


class Box(Rectangle):
    def __init__(self, length, width, height):
        Rectangle.__init__(self, length, width)
        self.__height = height

    def set_dimension(self, length, width, height):
        Rectangle.set_dimension(self, length, width)
        self.__height = height

    def get_height(self):
        return self.__height

    def area(self):
        return 2 * (self.get_length() * self.get_width() + self.get_length() * self.__height + self.get_width() * self.__height)

    def volume(self):
        return self.get_length() * self.get_width() * self.__height

    def print(self):
        print("Box 생성")
        print("Length = {}, Width = {}, Height = {}, Area = {}, Volume = {}".format(self.get_length(), self.get_width(), self.__height, self.area(), self.volume()))


if __name__ == "__main__":
    r = Rectangle(10, 20)
    r.print()

    b = Box(10, 20, 30)
    b.print()