import unittest


class TestPoint(unittest.TestCase):
    def test_default_case(self):
        from task3 import Point

        p = Point(x=21, y=42)
        self.assertEqual(p.x, 21)
        self.assertEqual(p.y, 42)
        self.assertIsInstance(Point, type)

    def test_no_self_in_code(self):
        import task3
        import inspect

        module_source_code = inspect.getsource(task3)
        self.assertNotIn("self.", module_source_code)
