# class Position:
#     def __init__(self, x: float, y: float) -> None:
#         self._x = x
#         self._y = y

#     def get_x(self) -> float:
#         return self._x

#     def get_y(self) -> float:
#         return self._y

#     def set_x(self, value: float) -> None:
#         self._x = value

#     def set_y(self, value: float) -> None:
#         self._y = value


# coord = Position(x=10.1, y=11.1)

# print(coord.get_x(), coord.get_y())

# coord.set_x(12.5), coord.set_y(15.5)

# print(coord.get_x(), coord.get_y())

# =================================================================


# class Position:
#     def __init__(self, x: float, y: float) -> None:
#         self._position_x = x
#         self._position_y = y

#     @property
#     def position_x(self):
#         print("Getting position x")
#         return self._position_x

#     @position_x.setter
#     def position_x(self, value):
#         print("Setting position x")
#         self._position_x = value

#     @position_x.deleter
#     def position_x(self):
#         print("Deleting position x")
#         del self._position_x


# pos = Position(x=5.2, y=18.3)

# print(pos.position_x)

# pos.position_x = 12.5

# print(pos.position_x)

# del pos.position_x


# =================================================================

#pavyzdys su inheritance
class Person:
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name) -> None:
        self._name = name

    @name.deleter
    def name(self) -> None:
        del self._name


class PersonOne(Person):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    @property
    def name(self):
        return super().name


person = PersonOne(name="Albert")
print(person.name)
person.name = "Jonas"
