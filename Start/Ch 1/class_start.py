# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ('HARDCOVER','SOFTCOVER','PAPERBAG')

    # TODO: double-underscore properties are hidden from other classes

    # TODO: create a class method

    # TODO: create a static method

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        if booktype not in Book.BOOK_TYPES:
            raise ValueError(f"{booktype} is not a valid booktype")
        else:
            self.booktype = booktype
        self.title = title


# TODO: access the class attribute
b1 = Book("wukong", "PAPERBAG")
b2 = Book("waseeeee","HARDCOVER")

# TODO: Create some book instances
print(b1.title)
print(b2.title)
# TODO: Use the static method to access a singleton object
