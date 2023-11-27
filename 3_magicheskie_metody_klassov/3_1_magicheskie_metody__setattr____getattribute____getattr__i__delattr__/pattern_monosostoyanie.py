class ThreadData:
    '''ПАТТЕРН МОНОСОСТОЯНИЕ'''
    __shared_attrs = {
        'name' : 'thread_1',
        'data' : {},
        'id' : 1
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs


th1 = ThreadData()
th2 = ThreadData()

th2.id = 3
th2.new = 'Новое свойство'


