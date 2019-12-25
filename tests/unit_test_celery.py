import unittest
import sys
sys.path.append(".")
from celery_queue.tasks import (celery, 
                                add, 
                                multiply, 
                                scrape)

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

class TestScrapeTask(unittest.TestCase):

    def setUp(self):
        self.task = scrape.apply_async()
        self.results = self.task.get()

    def test_task_state(self):
        self.assertEqual(self.task.state, "SUCCESS")

    def test_scraping(self):
        self.assertEqual(type(self.results), str)

if __name__ == '__main__':
    unittest.main()