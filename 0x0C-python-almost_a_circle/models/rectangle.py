from models import Base
class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__y = y
        self.__x = x
        super().__init__(id)

    def area(self):
        return self.__width * self.__height

    def display(self):
        string = ''
        print('\n' * self.y, end='')
        if self.__width != 0 and self.__height != 0:
            string += "\n".join(' ' * self.x + '#' * self.width
                                for j in range(self.__height))
        return string

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if not value > 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if not value > 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if not value > 0:
            raise ValueError("x must be > 0")

        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if not value > 0:
            raise ValueError("y must be > 0")

        self.__y = value

    def update(self, *args):
        count = 0
        for arg in args:
            count += 1
            if count == 1:
                self.id = args[0]
            elif count == 2:
                self.id = args[0]
                self.width = args[1]
            elif count == 3:
                self.id = args[0]
                self.width = args[1]
                self.height= args[2]
            elif count == 4:
                self.id = args[0]
                self.width = args[1]
                self.height= args[2]
                self.x= args[3]
            elif count == 5:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
    def to_dictionary(self):
        return {"id":self.id, "width":self.width, "height":self.height, "x":self.x, "y":self.y}

    def __str__(self):
        return f"[Recrangle] ({self.id}) {self.width}/{self.height}-{self.x}/{self.y}"

