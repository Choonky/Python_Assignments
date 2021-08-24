class Shape():

    def what_am_i(self):

        print('I am Shape')

       

class Rectangle(Shape):

    def __init__(self):

        pass

       

class Square(Shape):

    def __init__(self):

        pass



square = Square()

square.what_am_i()



rect = Rectangle()

rect.what_am_i()

