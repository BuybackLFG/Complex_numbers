import unittest
import math
from src.complex_n  import  Complex
from src.rational_n import Rational

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

    def test_large_real_part(self):
        # Проверка инициализации с очень большой действительной частью
        a = Complex(10**18, 0)
        self.assertEqual(a.real, Rational(10**18))
        self.assertEqual(a.imagine, Rational(0))

    def test_large_imaginary_part(self):
        # Проверка инициализации с очень большой мнимой частью
        a = Complex(0, 10**18)
        self.assertEqual(a.real, Rational(0))
        self.assertEqual(a.imagine, Rational(10**18))

    def test_large_addition(self):
        # Сложение комплексных чисел с очень большими частями
        a = Complex(10**18, 10**18)
        b = Complex(10**18, 10**18)
        result = a + b
        self.assertEqual(result.real, Rational(2 * 10**18))
        self.assertEqual(result.imagine, Rational(2 * 10**18))

    def test_large_subtraction(self):
        # Вычитание комплексных чисел с очень большими частями
        a = Complex(10**18, 10**18)
        b = Complex(10**18, 10**18)
        result = a - b
        self.assertEqual(result.real, Rational(0))
        self.assertEqual(result.imagine, Rational(0))

    def test_large_multiplication(self):
        # Умножение комплексных чисел с очень большими частями
        a = Complex(10**18, 10**18)
        b = Complex(10**18, 10**18)
        result = a * b
        self.assertEqual(result.real, Rational(0))
        self.assertEqual(result.imagine, Rational(2 * 10**36))

    def test_large_division(self):
        # Деление комплексных чисел с очень большими частями
        a = Complex(10**18, 10**18)
        b = Complex(10**18, 10**18)
        result = a / b
        self.assertAlmostEqual(float(result.real), 1.0)
        self.assertAlmostEqual(float(result.imagine), 0.0)

    def test_large_abs(self):
        # Проверка модуля комплексного числа с очень большими частями
        a = Complex(10**18, 10**18)
        self.assertAlmostEqual(abs(a), (2 * 10**36) ** 0.5)

    def test_large_pow(self):
        # Возведение комплексного числа с очень большими частями в степень
        a = Complex(10**18, 10**18)
        result = a ** 2
        self.assertEqual(result.real, Rational(0))
        self.assertEqual(result.imagine, Rational(2 * 10**36))

    def test_large_eq(self):
        # Проверка равенства комплексных чисел с очень большими частями
        a = Complex(10**18, 10**18)
        b = Complex(10**18, 10**18)
        self.assertTrue(a == b)

    def test_large_ne(self):
        # Проверка неравенства комплексных чисел с очень большими частями
        a = Complex(10**18, 10**18)
        b = Complex(10**18, 10**18 + 1)
        self.assertTrue(a != b)

    def test_large_neg(self):
        # Проверка унарного минуса для комплексного числа с очень большими частями
        a = Complex(10**18, 10**18)
        result = -a
        self.assertEqual(result.real, Rational(-10**18))
        self.assertEqual(result.imagine, Rational(-10**18))

    def test_large_arg(self):
        # Проверка аргумента комплексного числа с очень большими частями
        a = Complex(10**18, 10**18)
        self.assertAlmostEqual(a.arg(), math.pi / 4)

    def test_large_iadd(self):
        # Проверка сложения с присваиванием для комплексного числа с очень большими частями
        a = Complex(10**18, 10**18)
        b = Complex(10**18, 10**18)
        a += b
        self.assertEqual(a.real, Rational(2 * 10**18))
        self.assertEqual(a.imagine, Rational(2 * 10**18))

    def test_large_isub(self):
        # Проверка вычитания с присваиванием для комплексного числа с очень большими частями
        a = Complex(10**18, 10**18)
        b = Complex(10**18, 10**18)
        a -= b
        self.assertEqual(a.real, Rational(0))
        self.assertEqual(a.imagine, Rational(0))

    def test_large_imul(self):
        # Проверка умножения с присваиванием для комплексного числа с очень большими частями
        a = Complex(10**18, 10**18)
        b = Complex(10**18, 10**18)
        a *= b
        self.assertEqual(a.real, Rational(0))
        self.assertEqual(a.imagine, Rational(2 * 10**36))

    def test_large_itruediv(self):
        # Проверка деления с присваиванием для комплексного числа с очень большими частями
        a = Complex(10**18, 10**18)
        b = Complex(10**18, 10**18)
        a /= b
        self.assertAlmostEqual(float(a.real), 1.0)
        self.assertAlmostEqual(float(a.imagine), 0.0)


if __name__ == '__main__':
    unittest.main()