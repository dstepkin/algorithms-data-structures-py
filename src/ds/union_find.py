from typing import List


class UnionFind:
    def __init__(self, size: int) -> None:
        self.size: int = size
        self.sizes: List[int] = [1] * size
        self.ids: List[int] = list(range(size))
        self.component_amount: int = size

    def find(self, p: int) -> int:
        root: int = p
        while root != self.ids[root]:
            root = self.ids[root]
        while p != root:
            next_node: int = self.ids[p]
            self.ids[p] = root
            p = next_node
        return root

    def is_connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)

    def get_component_size(self, p: int) -> int:
        return self.sizes[self.find(p)]

    def get_size(self) -> int:
        return self.size

    def get_component_amount(self) -> int:
        return self.component_amount

    def unify(self, p: int, q: int) -> None:
        if self.is_connected(p, q):
            return
        root_p: int = self.find(p)
        root_q: int = self.find(q)
        if self.sizes[root_p] < self.sizes[root_q]:
            return self.unify(q, p)
        self.sizes[root_p] += self.sizes[root_q]
        self.ids[root_q] = root_p
        self.sizes[root_q] = 0
        self.component_amount -= 1
