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

