import math
from fractions import Fraction

class Rational:
    """
    Класс Rational представляет рациональное число (дробь) в виде числителя и знаменателя.
    Поддерживает арифметические операции, упрощение дробей и доступ к числителю и знаменателю через свойства.
    """
    def __init__(self, n: int | float, m: int | float = 1):
        """
        Инициализирует объект Rational.
        :param n: Числитель дроби.
        :param m: Знаменатель дроби (по умолчанию 1).
        :raises ValueError: Если знаменатель равен нулю.
        """
        if m == 0:
            raise ValueError('division by zero')
        if isinstance(n, float):
            frac = Fraction(n).limit_denominator()
            self.__numerator = frac.numerator
            self.__denominator = frac.denominator
        else:
            self.__numerator = n
            self.__denominator = m
        self._simplify()

    def _simplify(self):
        """
        Упрощает дробь, приводя её к несократимому виду.
        Если знаменатель отрицательный, меняет знаки числителя и знаменателя.
        """
        gcd_val = math.gcd(int(self.__numerator), int(self.__denominator))
        self.__numerator //= gcd_val
        self.__denominator //= gcd_val
        if self.__denominator < 0:
            self.__numerator = -self.__numerator
            self.__denominator = -self.__denominator

    @property
    def numerator(self):
        """
        Возвращает числитель дроби.
        :return: Числитель.
        """
        return self.__numerator

    @numerator.setter
    def numerator(self, value):
        """
        Устанавливает новое значение числителя и упрощает дробь.
        :param value: Новое значение числителя.
        """
        self.__numerator = value
        self._simplify()

    @property
    def denominator(self):
        """
        Возвращает знаменатель дроби.
        :return: Знаменатель.
        """
        return self.__denominator

    @denominator.setter
    def denominator(self, value):
        """
        Устанавливает новое значение знаменателя и упрощает дробь.
        :param value: Новое значение знаменателя.
        :raises ValueError: Если знаменатель равен нулю.
        """
        if value == 0:
            raise ValueError('denominator cannot be zero')
        self.__denominator = value
        self._simplify()

    def __add__(self, other):
        """
        Сложение двух рациональных чисел.

        :param other: Другое рациональное число или число типа int/float.
        :return: Результат сложения.
        """
        if isinstance(other, Rational):
            new_numerator = self.__numerator * other.__denominator + other.__numerator * self.__denominator
            new_denominator = self.__denominator * other.__denominator
            return Rational(new_numerator, new_denominator)
        elif isinstance(other, (int, float)):
            return Rational(self.__numerator + other * self.__denominator, self.__denominator)
        return NotImplemented

    def __sub__(self, other):
        """
        Вычитание двух рациональных чисел.
        :param other: Другое рациональное число или число типа int/float.
        :return: Результат вычитания.
        """
        if isinstance(other, Rational):
            new_numerator = self.__numerator * other.__denominator - other.__numerator * self.__denominator
            new_denominator = self.__denominator * other.__denominator
            return Rational(new_numerator, new_denominator)
        elif isinstance(other, (int, float)):
            return Rational(self.__numerator - other * self.__denominator, self.__denominator)
        return NotImplemented

    def __mul__(self, other):
        """
        Умножение двух рациональных чисел.
        :param other: Другое рациональное число или число типа int/float.
        :return: Результат умножения.
        """
        if isinstance(other, Rational):
            new_numerator = self.__numerator * other.__numerator
            new_denominator = self.__denominator * other.__denominator
            return Rational(new_numerator, new_denominator)
        elif isinstance(other, (int, float)):
            return Rational(self.__numerator * other, self.__denominator)
        return NotImplemented

    def __truediv__(self, other):
        """
        Деление двух рациональных чисел.
        :param other: Другое рациональное число или число типа int/float.
        :return: Результат деления.
        :raises ZeroDivisionError: Если делитель равен нулю.
        """
        if isinstance(other, Rational):
            if other.__numerator == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            new_numerator = self.__numerator * other.__denominator
            new_denominator = self.__denominator * other.__numerator
            return Rational(new_numerator, new_denominator)
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return Rational(self.__numerator, self.__denominator * other)
        return NotImplemented

    def __neg__(self):
        """
        Возвращает противоположное рациональное число.
        :return: Противоположное рациональное число.
        """
        return Rational(-self.__numerator, self.__denominator)

    def __eq__(self, other):
        """
        Проверяет равенство текущего рационального числа с другим числом.
        :param other: Другое рациональное число или число типа int/float.
        :return: True, если числа равны, иначе False. При несовместимых типах возвращает NotImplemented.
        """
        if isinstance(other, Rational):
            return self.__numerator == other.__numerator and self.__denominator == other.__denominator
        elif isinstance(other, (int, float)):
            return float(self) == other
        return NotImplemented

    def __float__(self):
        """
        Преобразует рациональное число в число с плавающей точкой.
        :return: Значение рационального числа как float.
        """
        return self.__numerator / self.__denominator

    def __abs__(self):
        """
        Возвращает модуль (абсолютное значение) рационального числа.
        :return: Новое рациональное число, представляющее модуль текущего числа.
        """
        return Rational(abs(self.__numerator), abs(self.__denominator))

    def __str__(self):
        """
        Возвращает строковое представление рационального числа.
        :return: Строковое представление дроби в формате "числитель/знаменатель".
                 Если знаменатель равен 1, возвращается только числитель.
        """
        if self.__denominator == 1:
            return str(self.__numerator)
        return f"{self.__numerator}/{self.__denominator}"

    def __repr__(self):
        """
        Возвращает формальное строковое представление объекта Rational.
        :return: Формальное представление объекта в формате "Rational(числитель, знаменатель)".
        """
        return f"Rational({self.__numerator}, {self.__denominator})"


class Complex:
    """
    Класс Complex представляет комплексное число в виде действительной и мнимой частей.
    Поддерживает арифметические операции, сравнение и другие математические операции.
    """
    def __init__(self, real: Rational | int | float, imagine: Rational | int | float = 0):
        """
        Инициализирует объект Complex.
        :param real: Действительная часть числа.
        :param imagine: Мнимая часть числа (по умолчанию 0).
        """
        self._real = Rational(real) if not isinstance(real, Rational) else real
        self._imagine = Rational(imagine) if not isinstance(imagine, Rational) else imagine

    @property
    def real(self):
        """
        Возвращает действительную часть комплексного числа.
        :return: Действительная часть.
        """
        return self._real

    @real.setter
    def real(self, value):
        """
        Устанавливает новое значение действительной части.
        :param value: Новое значение действительной части.
        """
        self._real = Rational(value) if not isinstance(value, Rational) else value

    @property
    def imagine(self):
        """
        Возвращает мнимую часть комплексного числа.
        :return: Мнимая часть.
        """
        return self._imagine

    @imagine.setter
    def imagine(self, value):
        """
        Устанавливает новое значение мнимой части.
        :param value: Новое значение мнимой части.
        """
        self._imagine = Rational(value) if not isinstance(value, Rational) else value

    def __str__(self):
        """
        Возвращает строковое представление комплексного числа.
        :return: Строковое представление.
        """
        if self.imagine.numerator == 0:
            return f'{self.real}'
        if self.imagine.numerator < 0:
            return f'{self.real} - {-self.imagine}i'
        return f'{self.real} + {self.imagine}i'

    def __repr__(self):
        """
        Возвращает формальное строковое представление объекта Complex.
        :return: Формальное строковое представление.
        """
        return f"Complex(real={self.real}, imagine={self.imagine})"

    def __add__(self, other):
        """
        Выполняет сложение двух комплексных чисел или комплексного числа с числом.
        :param other: Второе слагаемое.
        :return: Результат сложения.
        """
        if isinstance(other, self.__class__):
            return self.__class__(self.real + other.real, self.imagine + other.imagine)
        if isinstance(other, (int, float, Rational)):
            return self.__class__(self.real + other, self.imagine)
        return NotImplemented

    def __radd__(self, other):
        """
        Выполняет сложение числа с комплексным числом.
        :param other: Первое слагаемое.
        :return: Результат сложения.
        """
        return self.__add__(other)

    def __sub__(self, other):
        """
        Выполняет вычитание двух комплексных чисел или комплексного числа из числа.
        :param other: Вычитаемое.
        :return: Результат вычитания.
        """
        if isinstance(other, self.__class__):
            return self.__class__(self.real - other.real, self.imagine - other.imagine)
        if isinstance(other, (int, float, Rational)):
            return self.__class__(self.real - other, self.imagine)
        return NotImplemented

    def __rsub__(self, other):
        """
        Выполняет вычитание комплексного числа из числа.
        :param other: Уменьшаемое.
        :return: Результат вычитания.
        """
        return self.__class__(other) - self

    def __mul__(self, other):
        """
        Выполняет умножение двух комплексных чисел или комплексного числа на число.
        :param other: Множитель.
        :return: Результат умножения.
        """
        if isinstance(other, self.__class__):
            real = self.real * other.real - self.imagine * other.imagine
            imagine = self.real * other.imagine + self.imagine * other.real
            return self.__class__(real, imagine)
        if isinstance(other, (int, float, Rational)):
            return self.__class__(self.real * other, self.imagine * other)
        return NotImplemented

    def __rmul__(self, other):
        """
        Выполняет умножение числа на комплексное число.
        :param other: Множитель.
        :return: Результат умножения.
        """
        return self.__mul__(other)

    def __truediv__(self, other):
        """
        Выполняет деление двух комплексных чисел или комплексного числа на число.
        :param other: Делитель.
        :return: Результат деления.
        :raises ZeroDivisionError: Если делитель равен нулю.
        """
        if isinstance(other, self.__class__):
            denom = float(other.real) ** 2 + float(other.imagine) ** 2
            if denom == 0:
                raise ZeroDivisionError
            real = (float(self.real) * float(other.real) + float(self.imagine) * float(other.imagine)) / denom
            imagine = (float(self.imagine) * float(other.real) - float(self.real) * float(other.imagine)) / denom
            return self.__class__(real, imagine)
        if isinstance(other, (int, float, Rational)):
            if other == 0:
                raise ZeroDivisionError
            return self.__class__(self.real / other, self.imagine / other)
        return NotImplemented

    def __rtruediv__(self, other):
        """
        Выполняет деление числа на комплексное число.
        :param other: Делимое.
        :return: Результат деления.
        """
        return self.__class__(other) / self

    def __eq__(self, other):
        """
        Проверяет равенство двух комплексных чисел.
        :param other: Второе число.
        :return: True, если числа равны, иначе False.
        """
        if isinstance(other, self.__class__):
            return self.real == other.real and self.imagine == other.imagine
        return NotImplemented

    def __ne__(self, other):
        """
        Проверяет неравенство двух комплексных чисел.
        :param other: Второе число.
        :return: True, если числа не равны, иначе False.
        """
        if isinstance(other, self.__class__):
            return self.real != other.real or self.imagine != other.imagine
        return NotImplemented

    def __abs__(self):
        """
        Вычисляет модуль комплексного числа.
        :return: Модуль комплексного числа.
        """
        return (float(self.real) ** 2 + float(self.imagine) ** 2) ** 0.5

    def __pow__(self, n):
        """
        Выполняет возведение комплексного числа в степень.
        :param n: Целочисленный показатель степени (неотрицательный).
        :return: Результат возведения в степень.
        :raises ValueError: Если показатель степени отрицательный или не целый.
        """
        if not isinstance(n, int) or n < 0:
            raise ValueError("Exponent must be a non-negative integer")
        result = self.__class__(1, 0)
        base = self
        while n > 0:
            if n % 2 == 1:
                result *= base
            base *= base
            n //= 2
        return result

    def __iadd__(self, other):
        """
        Выполняет сложение с присваиванием.
        :param other: Второе слагаемое.
        :return: Изменённый объект.
        """
        if isinstance(other, self.__class__):
            self.real += other.real
            self.imagine += other.imagine
        elif isinstance(other, (int, float, Rational)):
            self.real += other
        else:
            return NotImplemented
        return self

    def __isub__(self, other):
        """
        Выполняет вычитание с присваиванием.
        :param other: Вычитаемое.
        :return: Изменённый объект.
        """
        if isinstance(other, self.__class__):
            self.real -= other.real
            self.imagine -= other.imagine
        elif isinstance(other, (int, float, Rational)):
            self.real -= other
        else:
            return NotImplemented
        return self

    def __imul__(self, other):
        """
        Выполняет умножение с присваиванием.
        :param other: Множитель.
        :return: Изменённый объект.
        """
        if isinstance(other, self.__class__):
            real = self.real * other.real - self.imagine * other.imagine
            imagine = self.real * other.imagine + self.imagine * other.real
            self.real = real
            self.imagine = imagine
        elif isinstance(other, (int, float, Rational)):
            self.real *= other
            self.imagine *= other
        else:
            return NotImplemented
        return self

    def __itruediv__(self, other):
        """
        Выполняет деление с присваиванием.
        :param other: Делитель.
        :return: Изменённый объект.
        :raises ZeroDivisionError: Если делитель равен нулю.
        """
        if isinstance(other, self.__class__):
            denom = float(other.real) ** 2 + float(other.imagine) ** 2
            if denom == 0:
                raise ZeroDivisionError
            real = (float(self.real) * float(other.real) + float(self.imagine) * float(other.imagine)) / denom
            imagine = (float(self.imagine) * float(other.real) - float(self.real) * float(other.imagine)) / denom
            self.real = real
            self.imagine = imagine
        elif isinstance(other, (int, float, Rational)):
            if other == 0:
                raise ZeroDivisionError
            self.real /= other
            self.imagine /= other
        else:
            return NotImplemented
        return self

    def __neg__(self):
        """
        Возвращает комплексное число, умноженное на -1.
        :return: Противоположное комплексное число.
        """
        return self.__class__(-self.real, -self.imagine)

    def arg(self):
        """
        Вычисляет аргумент комплексного числа (угол в радианах).
        :return: Аргумент комплексного числа.
        """
        return math.atan2(float(self.imagine), float(self.real))