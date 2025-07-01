import unittest
from unittest.mock import patch, MagicMock
from views.cli import CLI
from views.cli_concurrent import ConcurrentCLI

class TestStandardCLI(unittest.TestCase):
    @patch('views.cli.TaskController')  # ✅ patch before instantiating
    def setUp(self, MockController):
        self.mock_controller = MagicMock()
        MockController.return_value = self.mock_controller
        self.cli = CLI()

    def test_add_task(self):
        with patch('builtins.input', side_effect=["Test Title", "Test Description", "2025-12-31", "1", "y"]):
            self.cli.add_task()
        self.mock_controller.create_task.assert_called_once()

class TestConcurrentCLI(unittest.TestCase):
    @patch('views.cli_concurrent.TaskController')  # ✅ patch before instantiating
    def setUp(self, MockController):
        self.mock_controller = MagicMock()
        MockController.return_value = self.mock_controller
        self.cli = ConcurrentCLI()

    def tearDown(self):
        self.cli.running = False

    def test_add_task_concurrent(self):
        with patch('builtins.input', side_effect=["Concurrent Title", "Concurrent Description", "2025-12-31", "2", "y"]):
            self.cli.add_task()
        self.mock_controller.create_task.assert_called_once()

if __name__ == "__main__":
    unittest.main()
