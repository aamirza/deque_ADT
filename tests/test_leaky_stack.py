import unittest

from leaky_stack import LeakyStack


class LeakyStackTests(unittest.TestCase):
    def setUp(self) -> None:
        self.leaky_stack = LeakyStack(max_items=10)

    def test_leaky_stack_get_max_size(self):
        self.assertEqual(self.leaky_stack.max_size(), 10)

    def test_add_item(self):
        self.leaky_stack.push("google.com")
        self.assertEqual(self.leaky_stack.top(), 'google.com')

    def test_leaky_stack_size(self):
        self.assertEqual(self.leaky_stack.item_count(), 0)
        self.assertEqual(len(self.leaky_stack), 0)
        self.leaky_stack.push('google.com')
        self.assertEqual(len(self.leaky_stack), 1)

if __name__ == '__main__':
    unittest.main()
