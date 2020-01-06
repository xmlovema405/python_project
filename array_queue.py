from typing import Optional


class ArrayQueue:

    def __init__(self, capacity: int):
        self._items = []
        self._capacity = capacity
        self._head = 0
        self._tail = 0

    def enqueue(self, item: str) -> bool:
        if self._tail == self._capacity:
            if self._head == 0:
                return False
            else:
                for i in range(0, self._tail - self._head):
                    self._items[i] = self._items[i + self._head]
                self._tail = self._tail - self._head
                self._head = 0
        self._items.insert(self._tail, item)
        self._tail += 1
        return True

    def dequeue(self) -> Optional[str]:
        if self._head != self._tail:
            item = self._items[self._head]
            self._head += 1
            return item
        else:
            return None

    def __repr__(self) -> str:
        return " ".join(item for item in self._items[self._head: self._tail])


if __name__ == "__main__":
    arrayQueue = ArrayQueue(3)
    arrayQueue.enqueue('1')
    arrayQueue.enqueue('2')
    arrayQueue.enqueue('3')
    print(arrayQueue)
    arrayQueue.dequeue()
    print(arrayQueue)
    arrayQueue.enqueue('4')
    print(arrayQueue)
    print(arrayQueue.enqueue('5'))
    print(arrayQueue)