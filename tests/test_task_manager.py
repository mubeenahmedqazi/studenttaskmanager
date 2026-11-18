import unittest
from task_manager import tasks, add_task, complete_task, delete_task

class TestTaskManager(unittest.TestCase):
    
    def setUp(self):
        # Har test se pehle tasks list ko clear karein
        tasks.clear()

    def test_add_task(self):
        add_task("Learn Git and GitHub")
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["title"], "Learn Git and GitHub")
        self.assertFalse(tasks[0]["completed"])

    def test_complete_task(self):
        add_task("Write unit tests")
        task_id = tasks[0]["id"]
        complete_task(task_id)
        self.assertTrue(tasks[0]["completed"])

    def test_delete_task(self):
        add_task("Temporary task")
        task_id = tasks[0]["id"]
        delete_task(task_id)
        self.assertEqual(len(tasks), 0)

if __name__ == "__main__":
    unittest.main()