import unittest


class TestPerson(unittest.TestCase):
    def test_default_case(self):
        from task2 import Person

        p = Person(name="Thomas", surname="Thomson")
        self.assertEqual(p.name, "Thomas")
        self.assertEqual(p.surname, "Thomson")
        self.assertIsInstance(Person, type)
