"""Implement a stack and a queue with Python lists and collections.deque."""

from collections import deque


class Stack:
    """Last-in, first-out collection."""

    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self._items:
            raise IndexError("pop from an empty stack")
        return self._items.pop()

    def is_empty(self):
        return not self._items


class Queue:
    """First-in, first-out collection with efficient removal from the front."""

    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if not self._items:
            raise IndexError("dequeue from an empty queue")
        return self._items.popleft()

    def is_empty(self):
        return not self._items


if __name__ == "__main__":
    stack = Stack()
    stack.push("first")
    stack.push("last")
    print("Stack pop:", stack.pop())

    queue = Queue()
    queue.enqueue("first")
    queue.enqueue("last")
    print("Queue dequeue:", queue.dequeue())
