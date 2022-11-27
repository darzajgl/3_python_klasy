import unittest


class TestBee(unittest.TestCase):
    def test_default_case(self):
        from task5 import Bee

        bees = [
            Bee(name="Maja", identifier=222),
            Bee(name="Gucio", identifier=4234),
            Bee(name="Honey", identifier=1),
        ]

        expected_str_representations = [
            "222 Maja",
            "4234 Gucio",
            "1 Honey",
        ]

        for bee, str_representation in zip(bees, expected_str_representations):
            self.assertEqual(str(bee), str_representation)

        expected_hive = set(expected_str_representations)
        for bee in bees:
            self.assertEqual(bee.get_hive(), expected_hive)
