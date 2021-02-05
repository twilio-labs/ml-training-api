# src/test.py

import unittest
from unittest.mock import patch
from falcon import testing
from app import app, tasks


class TestAppRoutes(testing.TestCase):
    def setUp(self):
        super(TestAppRoutes, self).setUp()
        self.app = app

    def test_get_message(self):
        result = self.simulate_get('/ping')
        self.assertEqual(result.json, 'pong!')

## to do: update return value 
class TestCeleryTasks(unittest.TestCase):

    @patch('app.tasks.train')
    def test_mock_fib_task(self, mock_train):
        mock_train.run.return_value = []
        self.assertEqual(tasks.train.run(-1), [])


if __name__ == '__main__':
    unittest.main()
