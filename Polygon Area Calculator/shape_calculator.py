class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return self.width*2+self.height*2
    
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        output = ''
        for x in range(self.height):
            for y in range(self.width):
                output += '*'
            output += '\n'
        return output
    
    def get_amount_inside(self, shape):
        return (self.width // shape.width * self.height // shape.height)

    def __str__(self):
        if self.width != self.height:
            return 'Rectangle(width=' + str(self.width) + ', height=' + str(self.height) +')'
        else:
            return 'Square(side=' + str(self.width) + ')'

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return 'Square(side=' + str(self.width) + ')'
    
