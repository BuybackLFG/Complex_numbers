import unittest
import math
from src.complex_n  import Rational, Complex


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


class TestComplex(unittest.TestCase):
    def test_initialization(self):
        # Проверка инициализации с разными типами
        c1 = Complex(2, 3)
        self.assertIsInstance(c1.real, Rational)
        self.assertIsInstance(c1.imagine, Rational)

        c2 = Complex(Rational(1, 2), 4.5)
        self.assertEqual(c2.real, Rational(1, 2))
        self.assertEqual(c2.imagine, Rational(9, 2))

    def test_addition(self):
        c1 = Complex(1, 2)
        c2 = Complex(3, 4)
        result = c1 + c2
        self.assertEqual(result.real, Rational(4))
        self.assertEqual(result.imagine, Rational(6))

        # Проверка сложения с числом
        result = c1 + 5
        self.assertEqual(result.real, Rational(6))
        self.assertEqual(result.imagine, Rational(2))

        # Проверка правостороннего сложения
        result = 5 + c1
        self.assertEqual(result.real, Rational(6))
        self.assertEqual(result.imagine, Rational(2))

    def test_subtraction(self):
        c1 = Complex(5, 6)
        c2 = Complex(2, 3)
        result = c1 - c2
        self.assertEqual(result.real, Rational(3))
        self.assertEqual(result.imagine, Rational(3))

        # Проверка вычитания числа
        result = c1 - 2
        self.assertEqual(result.real, Rational(3))
        self.assertEqual(result.imagine, Rational(6))

        # Проверка правостороннего вычитания
        result = 10 - c1
        self.assertEqual(result.real, Rational(5))
        self.assertEqual(result.imagine, Rational(-6))

    def test_multiplication(self):
        c1 = Complex(1, 2)
        c2 = Complex(3, 4)
        result = c1 * c2
        self.assertEqual(result.real, Rational(-5))
        self.assertEqual(result.imagine, Rational(10))

        # Проверка умножения на число
        result = c1 * 2
        self.assertEqual(result.real, Rational(2))
        self.assertEqual(result.imagine, Rational(4))

    def test_division(self):
        c1 = Complex(1, 2)
        c2 = Complex(1, 1)
        result = c1 / c2
        self.assertEqual(result.real, Rational(3, 2))
        self.assertEqual(result.imagine, Rational(1, 2))

        # Проверка деления на число
        result = c1 / 2
        self.assertEqual(result.real, Rational(1, 2))
        self.assertEqual(result.imagine, Rational(1))

        # Проверка деления на ноль
        with self.assertRaises(ZeroDivisionError):
            c1 / 0

    def test_inplace_operations(self):
        c = Complex(2, 3)
        c += Complex(1, 1)
        self.assertEqual(c.real, Rational(3))
        self.assertEqual(c.imagine, Rational(4))

        c -= Complex(1, 1)
        self.assertEqual(c.real, Rational(2))
        self.assertEqual(c.imagine, Rational(3))

        c *= 2
        self.assertEqual(c.real, Rational(4))
        self.assertEqual(c.imagine, Rational(6))

    def test_abs(self):
        c = Complex(3, 4)
        self.assertEqual(abs(c), 5.0)

    def test_pow(self):
        c = Complex(1, 1)
        result = c ** 2
        self.assertEqual(result.real, Rational(0))
        self.assertEqual(result.imagine, Rational(2))

        # Проверка исключения при отрицательной степени
        with self.assertRaises(ValueError):
            c ** -1

    def test_arg(self):
        c = Complex(1, 1)
        self.assertAlmostEqual(c.arg(), math.pi / 4, places=5)

    def test_equality(self):
        c1 = Complex(2, 3)
        c2 = Complex(2, 3)
        c3 = Complex(3, 2)
        self.assertTrue(c1 == c2)
        self.assertTrue(c1 != c3)

    def test_string_representation(self):
        c1 = Complex(2, 3)
        self.assertEqual(str(c1), "2 + 3i")

        c2 = Complex(2, -3)
        self.assertEqual(str(c2), "2 - 3i")

        c3 = Complex(2, 0)
        self.assertEqual(str(c3), "2")


if __name__ == '__main__':
    unittest.main()