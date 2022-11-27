import unittest


class TestMyClass(unittest.TestCase):
    def test_default_case(self):
        from task1 import MyClass

        self.assertIsInstance(MyClass, type)
