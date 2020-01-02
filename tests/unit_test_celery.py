import unittest
import sys
sys.path.append(".")
sys.path.append("./celery_queue")
import pytest
from unittest.mock import patch
from unittest import TestCase
from celery import chain
from celery_queue import tasks
# from celery_queue.tasks import (celery, 
#                                 add, 
#                                 multiply, 
#                                 scrape)

# Ref of celery mock unit test
# - https://www.distributedpython.com/2018/05/15/testing-celery-chains/
# - https://www.distributedpython.com/2018/05/01/unit-testing-celery-tasks/
# - http://docs.celeryproject.org/en/latest/userguide/testing.html

class TestAddTask(unittest.TestCase):

    def test_task_state_and_addition(self):

        task = tasks.add.apply(args=[3, 5])
        self.assertEqual(task.status, "SUCCESS")
        self.assertEqual(task.result, 8)

class TestMultiplyTask(unittest.TestCase):

    def test_task_state_and_multiply(self):

        task = tasks.multiply.apply(args=[3, 5])
        self.assertEqual(task.status, "SUCCESS")
        self.assertEqual(task.result, 15)

class TestScrapeTask(unittest.TestCase):

    def test_task_state_and_scrape(self):
        
        task = tasks.scrape.apply()
        self.assertEqual(task.status, "SUCCESS")
        self.assertEqual(type(task.result), str)


class TestIndeedScrapTask(unittest.TestCase):

    def test_task_indeed_scrape(self):

        task = tasks.indeed_scrape.apply()
        self.assertEqual(task.status, "SUCCESS")
        self.assertEqual(type(task.result), type(None))

# class TestAddTask(unittest.TestCase):
#
#     def setUp(self):
#         self.task = add.apply_async(args=[3, 5])
#         self.results = self.task.get()
#
#     def test_task_state(self):
#         self.assertEqual(self.task.state, "SUCCESS")
#
#     def test_addition(self):
#         self.assertEqual(self.results, 8)
#
# class TestMultiplyTask(unittest.TestCase):
#
#     def setUp(self):
#         self.task = multiply.apply_async(args=[3, 5])
#         self.results = self.task.get()
#
#     def test_task_state(self):
#         self.assertEqual(self.task.state, "SUCCESS")
#
#     def test_multiplication(self):
#         self.assertEqual(self.results, 15)
#
# class TestScrapeTask(unittest.TestCase):
#
#     def setUp(self):
#         self.task = scrape.apply_async()
#         self.results = self.task.get()
#
#     def test_task_state(self):
#         self.assertEqual(self.task.state, "SUCCESS")
#
#     def test_scraping(self):
#         self.assertEqual(type(self.results), str)

if __name__ == '__main__':
    unittest.main()