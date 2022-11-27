import unittest
from task8 import Polynominal


class TestPlynominal(unittest.TestCase):
    def test_is_class(self):
        self.assertIsInstance(Polynominal, type)

    def test_instantiation(self):
        Polynominal()
        Polynominal(1, 2, 3)
        Polynominal(*range(100))
        Polynominal(0, 0, 0, 1, 0, 0)
        Polynominal(0, 0, 0, 1, -20, -10)

    def test_str_repr(self):
        test_cases = [
            ((), ""),
            ((0,), ""),
            ((0, 0, 0, 0, 0), ""),
            ((1, 1, 1), "1 + x + x^2"),
            ((0, 0, 1, 1, 1, 0, 0), "x^2 + x^3 + x^4"),
            ((10, 10, 1, 10), "10 + 10x + x^2 + 10x^3"),
            ((1, 2, -3, -2), "1 + 2x - 3x^2 - 2x^3"),
            ((-1, -1, 0, -1), "-1 - x - x^3"),
        ]

        for coefficients, str_repr in test_cases:
            with self.subTest(coefficients=coefficients, expected=str_repr):
                self.assertEqual(str(Polynominal(*coefficients)), str_repr)


class TestPolynominalComparision(unittest.TestCase):
    def test_comparision(self):
        test_cases = [
            ((), (), True),
            ((), (0, 0, 0), True),
            ((0, 0, 0, 0), (0,), True),
            ((), (1, 2, 3), False),
            ((0, 0, 0), (0, 0, 1), False),
            ((1, 2, 3), (1, 2, 3), True),
            ((-1, 1, 1), (-1, 1, 1), True),
            ((-1, 1, -1), (1, -1, 1), False),
        ]
        for coeffs_a, coeffs_b, expected in test_cases:
            with self.subTest(coeffs_a=coeffs_a, coeffs_b=coeffs_b, expected=expected):
                self.assertEqual(
                    Polynominal(*coeffs_a) == Polynominal(*coeffs_b), expected
                )


class TestPolynominalMethods(unittest.TestCase):
    def test_degree(self):
        test_cases = [
            ((), 0),
            ((0, 0, 0), 0),
            ((0,), 0),
            ((1, 2, 3), 2),
            ((0, 0, 0, 0, 1), 4),
            ((1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1), 10),
            ((0, 0, 0, -2), 3),
        ]
        for coeffs, expected_degree in test_cases:
            with self.subTest(
                coeffs=coeffs,
                expected_degree=expected_degree,
            ):
                self.assertEqual(Polynominal(*coeffs).get_degree(), expected_degree)

    def test_from_iterable(self):
        test_cases = [
            ([], ()),
            ((1, 2, 3), (1, 2, 3)),
            (range(5), (0, 1, 2, 3, 4)),
            (iter([1, 1, 1, 1]), (1, 1, 1, 1)),
        ]
        for iterable, expected_coeffs in test_cases:
            with self.subTest(
                iterable=iterable,
                expected_coeffs=expected_coeffs,
            ):
                self.assertEqual(
                    Polynominal.from_iterable(iterable), Polynominal(*expected_coeffs)
                )


class TestPolynominalOperations(unittest.TestCase):
    def test_addition(self):
        test_cases = [
            ((), (), ()),
            ((0,), (0, 0, 0), ()),
            ((1,), (1,), (2,)),
            ((1, 1, 1), (2, 1, 3), (3, 2, 4)),
            ((0, 1, 0, 1), (1, 0, 1, 0), (1, 1, 1, 1)),
            ((3, 3, 1, 2), (0, 0, 0, 0), (3, 3, 1, 2)),
            ((3, 2, 2, 1), (-3, -2, -2, -1), ()),
        ]
        for coeffs_a, coeffs_b, coeffs_expected in test_cases:
            with self.subTest(
                coeffs_a=coeffs_a, coeffs_b=coeffs_b, coeffs_expected=coeffs_expected
            ):
                self.assertEqual(
                    Polynominal(*coeffs_a) + Polynominal(*coeffs_b),
                    Polynominal(*coeffs_expected),
                )
