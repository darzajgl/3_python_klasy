import unittest


class TestAdder(unittest.TestCase):
    def test_default_case(self):
        from task4 import Adder

        a1 = Adder(10, 10)
        a2 = Adder(20, 20)

        self.assertEqual(a1.calculate(), 20)
        self.assertEqual(a2.calculate(), 40)

        self.assertIsInstance(Adder, type)
