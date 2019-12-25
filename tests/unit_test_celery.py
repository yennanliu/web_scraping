import unittest
import sys
sys.path.append(".")
from celery_queue.tasks import celery, add, multiply

class TestAddTask(unittest.TestCase):

    def setUp(self):
        self.task = add.apply_async(args=[3, 5])
        self.results = self.task.get()

    def test_task_state(self):
        self.assertEqual(self.task.state, "SUCCESS")

    def test_addition(self):
        self.assertEqual(self.results, 8)

class TestMultiplyTask(unittest.TestCase):

    def setUp(self):
        self.task = multiply.apply_async(args=[3, 5])
        self.results = self.task.get()

    def test_task_state(self):
        self.assertEqual(self.task.state, "SUCCESS")

    def test_multiplication(self):
        self.assertEqual(self.results, 15)

if __name__ == '__main__':
    unittest.main()