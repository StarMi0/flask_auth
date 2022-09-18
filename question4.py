import numpy as np
import matplotlib.pyplot as plt


class MyClass:
    """
    Question №4
    4. Создайте класс, в нем два метода. Вызовите нужный метод у создаваемого экземпляра класса,
    где название метода передано текстовой строкой минимум в двух вариантах исполнения. a = A('method1')
    """

    def __init__(self):
        self.x_min = 1
        self.x_max = 50

    def method1(self):
        x = np.arange(self.x_min, self.x_max, 0.01)
        plt.plot(x, np.sin(x))
        plt.xlabel(r'$x$')
        plt.ylabel(r'$f(x)$')
        plt.title(r'$f(x)=\sin(x)$')
        plt.grid(True)
        plt.show()

    def method2(self):
        x = np.arange(self.x_min, self.x_max, 0.01)
        plt.plot(x, np.cos(x))
        plt.xlabel(r'$x$')
        plt.ylabel(r'$f(x)$')
        plt.title(r'$f(x)=\cos(x)$')
        plt.grid(True)
        plt.show()


if __name__ == '__main__':
    A = MyClass()
    f1 = getattr(A, 'method1')()
    f2 = getattr(globals()['A'], 'method2')()

