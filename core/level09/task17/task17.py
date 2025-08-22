# Использование super() и MRO

# Создайте классы A, B, C, и D, где B и C наследуют от A, а D наследует от B и C.
# В каждом классе определите метод method, который выводит имя класса и вызывает метод super().method().
# Создайте экземпляр класса D и вызовите метод method, чтобы понять порядок вызова методов по MRO.

# Напишите тут ваш код
class A:
    def method(self):
        print("A")


class B(A):
    def method(self):
        print("B")
        super().method()


class C(A):
    def method(self):
        print("C")
        super().method()


class D(B, C):
    def method(self):
        print("D")
        super().method()

d = D()
d.method()
