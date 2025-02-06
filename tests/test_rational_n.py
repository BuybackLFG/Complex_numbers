import unittest
import math
from src.rational_n import Rational


class TestRational(unittest.TestCase):
    def test_initialization(self):
        # Проверка корректной инициализации
        r = Rational(2, 4)
        self.assertEqual(r.numerator, 1)
        self.assertEqual(r.denominator, 2)

        # Проверка исключения при нулевом знаменателе
        with self.assertRaises(ValueError):
            Rational(1, 0)

    def test_simplify(self):
        # Проверка упрощения дроби
        r = Rational(4, 6)
        self.assertEqual(r.numerator, 2)
        self.assertEqual(r.denominator, 3)

        # Проверка обработки отрицательного знаменателя
        r = Rational(3, -4)
        self.assertEqual(r.numerator, -3)
        self.assertEqual(r.denominator, 4)

    def test_properties(self):
        # Проверка сеттеров и упрощения
        r = Rational(1, 2)
        r.numerator = 6
        self.assertEqual(r.numerator, 3)
        self.assertEqual(r.denominator, 1)

        r.denominator = 4
        self.assertEqual(r.numerator, 3)
        self.assertEqual(r.denominator, 4)

        # Проверка исключения при установке нулевого знаменателя
        with self.assertRaises(ValueError):
            r.denominator = 0

    def test_string_representations(self):
        # Проверка строкового представления
        r1 = Rational(3, 1)
        self.assertEqual(str(r1), "3")
        self.assertEqual(repr(r1), "Rational(3, 1)")

        r2 = Rational(5, 2)
        self.assertEqual(str(r2), "5/2")
        self.assertEqual(repr(r2), "Rational(5, 2)")
    def test_large_simplification(self):
        # Проверка упрощения дробей с большими значениями
        a = Rational(10**18, 2 * 10**18)
        self.assertEqual(a.numerator, 1)
        self.assertEqual(a.denominator, 2)

    def test_large_addition(self):
        # Сложение больших дробей
        a = Rational(10**18, 2 * 10**18)
        b = Rational(10**18, 2 * 10**18)
        result = a + b
        self.assertEqual(result, Rational(1))

    def test_large_multiplication(self):
        # Умножение и упрощение больших дробей
        a = Rational(2 * 10**18, 3 * 10**18)
        b = Rational(3 * 10**18, 4 * 10**18)
        result = a * b
        self.assertEqual(result, Rational(1, 2))

    def test_large_equality(self):
        # Проверка равенства после упрощения
        a = Rational(2 * 10**18, 4 * 10**18)
        b = Rational(1, 2)
        self.assertEqual(a, b)

    def test_large_float_conversion(self):
        # Преобразование очень большой дроби в float
        a = Rational(12345678901234567890, 1)
        self.assertEqual(float(a), 12345678901234567890.0)

    def test_large_negative(self):
        # Работа с отрицательными большими числами
        a = Rational(-10**18, 2 * 10**18)
        self.assertEqual(a, Rational(-1, 2))

    def test_division_by_large(self):
        # Деление на большое число
        a = Rational(10**18, 1)
        result = a / 10**18
        self.assertEqual(result, Rational(1))

    def test_zero_division(self):
        # Проверка исключения при создании с нулевым знаменателем
        with self.assertRaises(ValueError):
            Rational(1, 0)
        # Проверка исключения при делении на ноль
        a = Rational(1)
        with self.assertRaises(ZeroDivisionError):
            a / Rational(0)

    def test_property_assignment(self):
        # Проверка установки больших значений через свойства
        a = Rational(1, 1)
        a.numerator = 2 * 10**18
        a.denominator = 4 * 10**18
        self.assertEqual(a, Rational(1, 2))

    def test_very_large_gcd(self):
        # Проверка НОД для очень больших взаимно простых чисел
        a = Rational(10**18 + 1, 10**18 + 3)
        self.assertEqual(a.numerator, 10**18 + 1)
        self.assertEqual(a.denominator, 10**18 + 3)

    def test_repr_large_numbers(self):
        # Проверка формального строкового представления
        a = Rational(10**18, 2 * 10**18)
        self.assertEqual(repr(a), "Rational(1, 2)")

if __name__ == '__main__':
    unittest.main()
