import unittest

from deque import ArrayDeque, Empty


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.d = ArrayDeque()

    def test_add_first_adds_to_the_left(self):
        self.d.add_first(8)
        self.assertEqual(self.d.first(), 8)

    def test_correct_length(self):
        self.assertEqual(len(self.d), 0)
        self.d.add_first(5)
        self.assertEqual(len(self.d), 1)
        self.d.add_first(6)
        self.assertEqual(len(self.d), 2)

    def test_add_first_twice_adds_to_the_left_twice(self):
        self.d.add_first(5)
        self.d.add_first(9)
        self.assertEqual(self.d.first(), 9)

    def test_add_last_twice_adds_to_the_right_twice(self):
        self.d.add_last(5)
        self.d.add_last(9)
        self.assertEqual(self.d.last(), 9)

    def test_adding_first_and_last(self):
        self.d.add_first(9)
        self.d.add_last(7)
        self.assertEqual(7, self.d.last())
        self.assertEqual(9, self.d.first())
        self.d.add_last(6)
        self.assertEqual(6, self.d.last())

    def test_first_returns_error_if_empty(self):
        with self.assertRaisesRegex(Empty, "The deque is empty"):
            self.d.first()

    def test_last_returns_error_if_empty(self):
        with self.assertRaisesRegex(Empty, "The deque is empty"):
            self.d.last()

    def test_is_empty(self):
        self.assertTrue(self.d.is_empty())

    def test_when_first_is_also_last(self):
        self.d.add_first(7)
        self.assertEqual(self.d.first(), 7)
        self.assertEqual(self.d.last(), 7)
        self.d.add_first(5)
        self.assertEqual(self.d.last(), 7)

    def test_when_last_is_also_first(self):
        self.d.add_last(5)
        self.assertEqual(self.d.first(), 5)
        self.d.add_last(9)
        self.assertEqual(self.d.first(), 5)

    def test_delete_first_removes_first(self):
        self.d.add_first(7)
        self.assertEqual(self.d.delete_first(), 7)

    def test_delete_first_deletes_last_if_its_the_only_element(self):
        self.d.add_last(6)
        self.assertEqual(self.d.delete_first(), 6)

    def test_delete_first_deletes_last_and_reports_accurate_size(self):
        self.d.add_last(6)
        self.d.delete_first()
        self.assertEqual(len(self.d), 0)

    def test_raise_error_if_deleting_from_empty_list(self):
        with self.assertRaises(Empty):
            self.d.delete_first()

    def test_delete_first_makes_first_empty(self):
        self.d.add_first(7)
        self.d.delete_first()
        with self.assertRaises(Empty):
            self.d.first()


if __name__ == '__main__':
    unittest.main()
