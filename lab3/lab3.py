class DFSIterator:
    """Class to traverse the binary heap depth-first .

    Attributes:
        stack: list with result of in-depth traversal
        lst: list of heap elements
    """

    def __init__(self, lst):
        self.stack = []
        self.lst = lst
        self.push_left(0)

    def next(self):
        """Method to acquire next element

        Returns:
            Node key and value in tuple data type
        """
        idx = self.stack.pop()
        self.push_left(idx * 2 + 2)
        return self.lst[idx].key, self.lst[idx].value

    def hasNext(self):
        """Method to find out is there next element

        Returns:
            Boolean value True if there is next element available or False if there isn't
        """
        return len(self.stack) > 0

    def push_left(self, start):
        """Method for realisation of in-depth traversal

        Args:
            start: number of element in heap list from which traverse will be started
        """
        idx = start
        while idx < len(self.lst):
            self.stack.append(idx)
            idx = idx * 2 + 1


class BFSIterator:
    """Class to traverse the binary heap in broadwise.

    Attributes:
        i: number of element in list of heap elements from which traverse will be continued
        lst: list of heap elements
    """

    def __init__(self, lst):
        self.i = -1
        self.lst = lst

    def next(self):
        """Method to acquire next element

        Returns:
            Node key and value in tuple data type
        """
        self.i += 1
        return self.lst[self.i].key, self.lst[self.i].value

    def hasNext(self):
        """Method to find out is there next element

        Returns:
            Boolean value True if there is next element available or False if there isn't
        """
        return self.i + 1 < len(self.lst)


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Heap:
    """Class that realises max-heap data storage.

    Attributes:
        lst: list of elements
    """

    def __init__(self):
        self.lst = []

    def contains(self, key):
        """Method to find element by its data key

        Args:
            key: data key to be searched
        Returns:
            Boolean value True if there is such element available or False if there isn't
        """
        for node in self.lst:
            if node.key == key:
                return True
        return False

    def insert(self, node):
        """Method to add new element to heap

        Args:
            node: new node to be inserted to the heap
        """
        self.lst.append(node)
        idx = len(self.lst) - 1
        self.heapifyUp(idx)

    def heapifyDown(self, idx):
        """Method to heap ordering from top to bottom

        Args:
            idx: position of the current root
        """
        n = len(self.lst)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            large = idx
            if left < n:
                if self.lst[left].key > self.lst[large].key:
                    large = left
            if right < n:
                if self.lst[right].key > self.lst[large].key:
                    large = right
            if large == idx:
                break
            else:
                self.lst[idx], self.lst[large] = self.lst[large], self.lst[idx]
                idx = large

    def heapifyUp(self, idx):
        """Method to heap ordering from bottom to top

        Args:
            idx: position of the current root
        """
        parent = (idx - 1) // 2
        while idx > 0 and self.lst[parent].key < self.lst[idx].key:
            self.lst[idx], self.lst[parent] = self.lst[parent], self.lst[idx]
            idx = parent
            parent = (idx - 1) // 2

    def getRoot(self):
        """Method to acquire current maximum (root) of the heap

        Returns:
            node of the current root

        Raises:
            Exception:if heap is empty
        """

        if len(self.lst) == 0:
            raise Exception("heap is empty")
        res = self.lst[0]
        self.lst[0] = self.lst[len(self.lst) - 1]
        self.lst = self.lst[:-1]
        self.heapifyDown(0)
        return res

    def remove(self, key):
        """Method to remove element from the heap by its key value

        Args:
            key: Data key of the element to be removed from the heap
        """
        for idx in range(len(self.lst)):

            if self.lst[idx].key == key:

                self.lst[0], self.lst[idx] = self.lst[idx], self.lst[0]
                self.lst[0] = self.lst[len(self.lst) - 1]
                self.lst.pop()

                if idx >= len(self.lst):
                    return

                self.heapifyUp(idx)

                self.heapifyUp(idx)
                return

    def create_dft_iterator(self):
        """Method to create iterator to traverse the heap in depth class object

        Returns:
            Object of the DFSIterator class initialized by current heap data list
        """
        return DFSIterator(self.lst)

    def create_bft_iterator(self):
        """Method to create iterator to traverse the heap in broadwise class object

        Returns:
            Object of the BFSIterator class initialized by current heap data list
        """
        return BFSIterator(self.lst)



