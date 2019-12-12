import sys
import os


class LinkedListNode(object):
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.pre = None
        self.nxt = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hkeys = {}
        self.top = LinkedListNode(None, -1)
        self.tail = LinkedListNode(None, -1)
        self.top.nxt = self.tail
        self.tail.pre = self.top

    def get(self, key: int) -> int:
        if key in self.hkeys.keys():
            cur = self.hkeys[key]
            cur.pre.nxt = cur.nxt
            cur.nxt.pre = cur.pre

            top_node = self.top.nxt
            cur.nxt = top_node
            cur.pre = self.top
            self.top.nxt = cur
            top_node.pre = cur
            return self.hkeys[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hkeys.keys():
            cur = self.hkeys[key]
            cur.value = value
            cur.pre.nxt = cur.nxt
            cur.nxt.pre = cur.pre

            top_node = self.top.nxt
            cur.nxt = top_node
            cur.pre = self.top
            self.top.nxt = cur
            top_node.pre = cur
        else:
            cur = LinkedListNode(key, value)
            self.hkeys[key] = cur

            top_node = self.top.nxt
            cur.nxt = top_node
            cur.pre = self.top
            self.top.nxt = cur
            top_node.pre = cur
            if len(self.hkeys.keys()) > self.capacity:
                self.hkeys.pop(self.tail.pre.key)
                self.tail.pre.pre.nxt = self.tail
                self.tail.pre = self.tail.pre.pre

    def __repr__(self):
        vals = []
        p = self.top.nxt
        while p.nxt:
            vals.append(str(p.value))
            p = p.nxt
        return '->'.join(vals)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache)
    cache.get(1)  # 返回  1
    cache.put(3, 3)  # 该操作会使得密钥 2 作废
    print(cache)
    cache.get(2)  # 返回 -1 (未找到)
    cache.put(4, 4)  # 该操作会使得密钥 1 作废
    print(cache)
    cache.get(1)  # 返回 -1 (未找到)
    cache.get(3)  # 返回  3
    print(cache)
    cache.get(4)  # 返回  4
    print(cache)
