class Node:
    """Class for nodes for self-written bidirectional list .

       Attributes:
           key: Information in the node.
           next: Pointer to the next node.
           prev: Pointer to the previous node.
    """

    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None


class List:
    """Class for self-written bidirectional list .

    Realized methods:
        push_back(self,key)
        push_front(self,key)
        pop_back(self)
        pop_front(self)
        insert(self,key,i)
        at(self,i)
        remove(self,i)
        get_size(self)
        clear(self)
        set(self,i,key)
        isEmpty(self)
        contains(self,lst)
        __str__(self):

    Attributes:
        head: Pointer to the head of the list.
        tail: Pointer to the end of the list.
        size: An integer count of nodes in the list.
    """

    def __init__(self):
        """Inits List.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def push_back(self, key):
        """Create new node with information from argument key and push it to the end of the list.

        Args:
            key: Information to be saved in created node
        """
        n = Node(key)

        if self.head:
            self.tail.next = n
            n.prev = self.tail
            self.tail = n
        else:
            self.head = self.tail = n
        self.size += 1

    def push_front(self, key):
        """Create new node with information from argument key and push it to the start of the list.

        Args:
            key: Information to be saved in created node
        """
        n = Node(key)

        if self.head:
            n.next = self.head
            self.head.prev = n
            self.head = n
        else:
            self.head = self.tail = n
        self.size += 1

    def pop_back(self):
        """Delete element from the end of the list.

        Raises:
            Exception: if list is empty
        """
        if self.head:

            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            self.size -= 1
        else:
            raise Exception("list is empty")

    def pop_front(self):
        """Delete element from the start of the list.

        Raises:
            Exception: if list is empty
        """
        if self.head:

            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.size -= 1
        else:
            raise Exception("list is empty")

    def insert(self, key, idx):
        """Create new node with information from argument key and push it in the desired place of the list.

        Args:
            key: Information to be saved in created node
            idx: Number of list element where new node will be inserted

        Raises:
            Exception: if number of the list element is incorrect
        """
        n = Node(key)
        if self.head:
            cur = self.head
            while cur and idx > 0:
                idx -= 1
                cur = cur.next

            if cur:

                if cur == self.head:
                    self.push_front(key)
                else:
                    cur.prev.next = n
                    n.prev = cur.prev
                    n.next = cur
                    cur.prev = n
                    self.size += 1
            else:
                raise Exception("incorrect index")
        else:
            self.head = self.tail = n
            self.size += 1

    def at(self, idx):
        """Get data from the list element by its number in the list.

        Args:
            idx: Number of list element
        Returns
            cur.key: data from the node on the i'th place in the list

        Raises:
            Exception: if number of the list element is incorrect
        """
        cur = self.head
        while cur and idx > 0:
            idx -= 1
            cur = cur.next
        if cur:
            return cur.key
        else:
            raise Exception("incorrect index")

    def remove(self, idx):
        """Delete list element by its number in the list.

        Args:
            idx: Number of list element

        Raises:
            Exception: if number of the list element is incorrect
        """
        cur = self.head
        while cur and idx > 0:
            idx -= 1
            cur = cur.next
        if cur:

            if cur == self.head:
                self.pop_front()

            elif cur == self.tail:
                self.pop_back()

            else:
                cur.next.prev = cur.prev
                cur.prev.next = cur.next
                self.size -= 1
        else:
            raise Exception("incorrect index")

    def get_size(self):
        """Get list size.

        Returns:
            Size of the current list
        """
        return self.size

    def clear(self):
        """Clear all elements of the current list.
        """
        self.head = self.tail = None
        self.size = 0

    def set(self, idx, key):
        """Change information in the node from desired place of the list.

        Args:
            key: Information to be saved in node
            idx: Number of list element where information will be changed

        Raises:
            Exception: if number of the list element is incorrect
        """
        cur = self.head
        while cur and idx > 0:
            idx -= 1
            cur = cur.next
        if cur:
            cur.key = key
        else:
            raise Exception("incorrect index")

    def isEmpty(self):
        """Check list if it is empty.

        Returns:
            Boolean value true equals list is empty and false if list isn't empty
        """
        return self.size == 0

    def contains(self, lst):
        """Check if list contains other list.

        Args:
            lst: the list to be searched for
        Returns:
            Boolean value true if current list contains list from lst argument and false if not
        """
        idx = lst.head
        while idx:
            j = self.head
            while j:

                if j.key == idx.key:
                    break
                j = j.next

            if j is None:
                return False
            idx = idx.next
        return True

    def __str__(self):
        """Compute the string representation of current list.

         Returns:
             string object with information from all nodes of current list
         """
        cur = self.head
        res = ""
        while cur:
            res += str(cur.key)
            res += " "
            cur = cur.next
        return res.rstrip()


if __name__ == '__main__':
    arr1 = input('Введите элементы 1-го списка через пробел: ')
    arr2 = input('Введите элементы 2-го списка через пробел: ')
    lst1 = List()
    lst2 = List()
    for i in arr1.split(' '):
        lst1.push_back(int(i))
    for i in arr2.split(' '):
        lst2.push_back(int(i))
    print('Список 1:', str(lst1))
    print('Список 2:', str(lst2))

    lst1.push_front(100)
    print('Вставка в начало числа 100:', str(lst1))
    lst1.pop_back()
    print('Удаление с конца:', str(lst1))
    lst1.pop_front()
    print('Удаление из начала:', str(lst1))
    lst1.insert(200, 1)
    print('Вставка числа 200 на вторую позицию:', str(lst1))
    lst1.remove(2)
    print('Удаление третьего элемента:', str(lst1))
    print('Размер первого списка:', lst1.get_size())
    lst1.set(0, -5)
    print('Заменяем 1 элемент на -5:', str(lst1))
    print(
        'Проверяем содержит ли первый список второй список:',
        lst1.contains(lst2))
    lst1.clear()
    lst2.clear()
    print(
        'Очищаем оба списка теперь их размеры:',
        lst1.get_size(),
        lst2.get_size())
