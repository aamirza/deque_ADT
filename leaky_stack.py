class LeakyStack:
    def __init__(self, max_items):
        self._items = []
        self._max_size = max_items
        self._size = 0

    def __len__(self):
        return self._size

    def item_count(self):
        return len(self)

    def max_size(self):
        return self._max_size

    def top(self):
        return self._items[-1]

    def push(self, element):
        self._items.append(element)
        self._size += 1
