import unittest
from task6 import Colony, Ant


class TestAntColony(unittest.TestCase):
    def test_default_case(self):
        self.assertIsInstance(Colony, type)
        self.assertIsInstance(Ant, type)

    def test_empty_colony(self):
        colony = Colony("my-colony")
        self.assertEqual(colony.name, "my-colony")
        self.assertEqual(colony.ants, set())

    def test_ant_spawning(self):
        colony = Colony("my-colony")
        worker = colony.spawn_ant("worker")
        self.assertEqual(worker.name, "worker")
        self.assertIs(worker.colony, colony)
        self.assertEqual(colony.ants, {worker})

    def test_multiple_colonies(self):
        colony_alpha = Colony("alpha")
        colony_beta = Colony("beta")
        alpha_worker = colony_alpha.spawn_ant("worker")

        self.assertIs(alpha_worker.colony, colony_alpha)
        self.assertEqual(colony_alpha.ants, {alpha_worker})
        self.assertEqual(colony_beta.ants, set())

        beta_worker = colony_beta.spawn_ant("worker")
        self.assertIs(beta_worker.colony, colony_beta)
        self.assertEqual(colony_alpha.ants, {alpha_worker})
        self.assertEqual(colony_beta.ants, {beta_worker})

    def test_multiple_ants(self):
        colony = Colony("my-colony")
        self.assertEqual(colony.ants, set())

        workers = [
            colony.spawn_ant("worker_alpha"),
            colony.spawn_ant("worker_beta"),
            colony.spawn_ant("worker_gamma"),
        ]

        for worker in workers:
            self.assertIs(worker.colony, colony)

        self.assertEqual(colony.ants, set(workers))
