import unittest
from models import storage
from models.state import State

class TestFileStorage(unittest.TestCase):
    def test_get(self):
        new_state = State(name="California")
        storage.new(new_state)
        storage.save()
        self.assertEqual(storage.get(State, new_state.id), new_state)
        self.assertIsNone(storage.get(State, "nonexistent_id"))

    def test_count(self):
        initial_count = storage.count(State)
        new_state = State(name="California")
        storage.new(new_state)
        storage.save()
        self.assertEqual(storage.count(State), initial_count + 1)
        self.assertEqual(storage.count(), initial_count + 1)  # Assuming no other objects are added in the meantime

