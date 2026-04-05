#Operator overloading is a feature in Python that lets you change how built-in  operators (like +, -, *, /, ==, <, [], etc.)
# work for your own custom classes.
'''
| Operator            | Special Method             | Example     |
| ------------------- | -------------------------- | ----------- |
| `+`                 | `__add__(self, other)`     | `v1 + v2`   |
| `-`                 | `__sub__(self, other)`     | `v1 - v2`   |
| `*`                 | `__mul__(self, other)`     | `v1 * v2`   |
| `/`                 | `__truediv__(self, other)` | `v1 / v2`   |
| `==`                | `__eq__(self, other)`      | `v1 == v2`  |
| `<`                 | `__lt__(self, other)`      | `v1 < v2`   |
| `str()` / `print()` | `__str__(self)`            | `print(v1)` |

'''
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __add__(self, other):
    #     return f"{self.x + other.x}i+{self.y + other.y}j"
    # return srting

    def __str__(self):
        return f"{self.x}i+ {self.y}j"

    def __add__(self, other):#------->operator overloading
        return Vector(self.x + other.x, self.y + other.y)
    #returns vector


v1=Vector(1,2)
v2=Vector(3,4)

print(v1)
print(v2)
print(v1 + v2)

print(type(v1+v2))