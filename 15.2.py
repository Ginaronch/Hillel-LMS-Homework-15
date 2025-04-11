class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Знаменатель не может быть нулем")
        elif a >= b:
            raise ValueError("Это неправильная дробь(числитель должен быть меньше знаменателя)")
        self.a = a
        self.b = b

    def __mul__(self, other):
        return Fraction(self.a * other.a,  self.b * other.b)

    def __add__(self, other):
        if self.b != other.b:
            ob_zn = self.b * other.b
            ch1 = self.a * other.b
            ch2 = other.a * self.b
            ob_ch = ch1 + ch2
        else:
            ob_zn = self.b
            ob_ch = self.a + other.a
        return Fraction(ob_ch, ob_zn)

    def __sub__(self, other):
        if self.b != other.b:
            ob_zn = self.b * other.b
            ch1 = self.a * other.b
            ch2 = other.a * self.b
            ob_ch = ch1 - ch2
        else:
            ob_zn = self.b
            ob_ch = self.a - other.a
        return Fraction(ob_ch, ob_zn)

    def __eq__(self, other):
        return self.a * other.b == self.b * other.a

    def __gt__(self, other):
        return self.a * other.b > self.b * other.a

    def __lt__(self, other):
        return self.a * other.b < self.b * other.a

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
try:
    f_c = f_b + f_a
except ValueError as e:
    print(e)
try:
    f_d = Fraction(3, 0)
except ValueError as e:
    print(e)
f_e = f_b * f_a
assert str(f_e) == 'Fraction: 6, 18'
f_f = f_a - f_b
assert str(f_f) == 'Fraction: 3, 18'
assert f_f < f_e # True
assert f_e > f_f  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')