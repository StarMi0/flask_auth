

class Base(object):
    """
    Question №5
    5. Создайте класс с наследованием от двух других классов. Расскажите про роль функции super()
    """
    def __init__(self):
        print('Base.__init__')


class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')


class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')


class C(A, B):
    def __init__(self):
        super().__init__()
        print('C.__init__')


if __name__ == '__main__':
    x = C()