# Should have the following methods, and perform most in O(1) time.

# add_first
# add_last
# delete_first
# delete_last
# first()
# last()
# is_empty
# len

class Empty(Exception):
    pass


class ArrayDeque:
    def __init__(self):
        self._first = []
        self._first_index = 0
        self._last = []
        self._last_index = 0
        self.size = 0

    def __len__(self):
        return self.size

    def _first_is_empty(self):
        return len(self._first) <= self._first_index

    def _last_is_empty(self):
        return len(self._last) == self._last_index

    def add_first(self, e):
        self._first.append(e)
        self.size += 1

    def add_last(self, e):
        self._last.append(e)
        self.size += 1

    def first(self):
        if self.is_empty():
            raise Empty("The deque is empty.")
        if not self._first_is_empty():
            return self._first[-1 - self._first_index]
        else:
            return self._last[self._last_index]

    def last(self):
        if self.is_empty():
            raise Empty("The deque is empty.")
        if not self._last_is_empty():
            return self._last[-1 - self._last_index]
        else:
            return self._first[self._first_index]

    def is_empty(self):
        return len(self) == 0

    def delete_first(self):
        if self.is_empty():
            raise Empty("The deque is empty.")
        if not self._first_is_empty():
            self.size -= 1
            return self._first.pop()
        else:
            value = self._last[self._last_index]
            self._last[self._last_index] = None
            self._last_index += 1
            self.size -= 1
            return value

    def delete_last(self):
        if self.is_empty():
            raise Empty("The deque is empty.")
        if not self._last_is_empty():
            self.size -= 1
            return self._last.pop()
        else:
            value = self._first[self._first_index]
            self._first[self._first_index] = None
            self._first_index += 1
            self.size -= 1
            return value
