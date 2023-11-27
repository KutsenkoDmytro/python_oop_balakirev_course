class Node:
    '''Отвечает за отдельный элемент двусвязного списка.'''

    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class LinkedList:
    '''Описывает базовые операции с двусвязным списком.'''

    def __init__(self):
        self.head = None
        self.tail = None

    def __del__(self):
        while self.head != None:
            self.pop_front()

    def push_front(self, data):
        '''добавляет элемент в начало списка'''
        ptr = data
        ptr.next = self.head
        if self.head != None:
            self.head.prev = ptr
        if self.tail == None:
            self.tail = ptr
        self.head = ptr

    def push_back(self, data):
        '''добавляет элемент в конец списка'''
        ptr = data
        ptr.prev = self.tail
        if self.tail != None:
            self.tail.next = ptr
        if self.head == None:
            self.head = ptr
        self.tail = ptr

    def pop_front(self):
        '''удаляет первый элемент списка'''
        if self.head == None:
            return
        ptr = self.head.next
        if ptr != None:
            ptr.prev = None
        else:
            self.tail = None
        del self.head
        self.head = ptr

    def pop_back(self):
        '''удаляет последний элемент списка'''
        if self.tail == None:
            return
        ptr = self.tail.prev
        if ptr != None:
            ptr.next = None
        else:
            self.head = None
        del self.tail
        self.tail = ptr

    def getAt(self, index):
        '''метод для доступа к произвольному элементу списка'''
        ptr = self.head
        n = 0
        while n != index:
            if ptr == None:
                return ptr
            ptr = ptr.next
            n += 1
        return ptr

    def insert(self, index, data):
        '''метод для промежуточной вставки элемента в список.'''
        right = self.getAt(index)
        if right == None:
            return self.push_back(data)  # вставка в конец списка.

        left = right.prev
        if left == None:
            return self.push_front(data)  # вставка в начало списка.

        ptr = data
        ptr.prev = left
        ptr.next = right
        left.next = ptr
        right.prev = ptr

        return ptr

    def earse(self, index):
        '''метод для удаления промежуточного элемента списка.'''
        ptr = self.getAt(index)
        if ptr == None:
            return
        if ptr.prev == None:  # если собираемся удалить первый элемент
            self.pop_front()
            return
        if ptr.next == None:  # если собираемся удалить последний элемент
            self.pop_back()
            return

        left = ptr.prev
        right = ptr.next

        left.next = right
        right.prev = left

        del ptr



# #Для проверки.
# lst = LinkedList()
# lst.push_back(Node("данные 1"))
# lst.push_back(Node("данные 2"))
# lst.push_back(Node("данные 3"))
# lst.push_back(Node("данные 4"))
# lst.push_front(Node("данные 4"))
# lst.earse(2)
#
# for i in range(4):
#     print(lst.getAt(i).data)
