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
        self._last = []
        self.size = 0

    def __len__(self):
        return len(self._first) + len(self._last)

    def _first_is_empty(self):
        return len(self._first) == 0

    def _last_is_empty(self):
        return len(self._last) == 0

    def add_first(self, e):
        self._first.append(e)

    def add_last(self, e):
        self._last.append(e)

    def first(self):
        if self.is_empty():
            raise Empty("The deque is empty.")
        if not self._first_is_empty():
            return self._first[-1]
        else:
            return self._last[0]

    def last(self):
        if self.is_empty():
            raise Empty("The deque is empty.")
        if not self._last_is_empty():
            return self._last[-1]
        else:
            return self._first[0]

    def is_empty(self):
        return len(self) == 0

    def delete_first(self):
        if self.is_empty():
            raise Empty("The deque is empty.")
        if not self._first_is_empty():
            return self._first.pop()
        else:
            value = self._last[0]
            self._last[0] = None
            return value
