'''
Большой подвиг 9. (task_6.py)

Используя механизм наследования, вам поручено разработать функционал по построению моделей нейронных сетей. Общая схема модели очень простая:

NetworkLayer

Базовый класс Layer имеет локальный атрибут next_layer, который ссылается на следующий объект слоя нейронной сети (объект класса Layer или любого объекта дочерних классов). У последнего слоя значение next_layer = None.

Создавать последовательность слоев предполагается командами:

first_layer = Layer()
next_layer = first_layer(Layer())
next_layer = next_layer(Layer())
...
То есть, сначала создается объект first_layer класса Layer, а затем он вызывается как функция для образования связки со следующим слоем. При этом возвращается ссылка на следующий слой и переменная next_layer ссылается уже на этот следующий слой нейронной сети. И так можно создавать столько слоев, сколько необходимо.

В каждом объекте класса Layer также должен формироваться локальный атрибут:

name = 'Layer'
Но сам по себе класс Layer образует только связи между слоями. Никакой другой функциональности он не несет. Чтобы это исправить, в программе нужно объявить еще два дочерних класса:

Input - формирование входного слоя нейронной сети;
Dense - формирование полносвязного слоя нейронной сети.

NetworkClasses

Конечно, создавать нейронную сеть мы не будем. Поэтому, в классе Input нужно лишь прописать инициализатор так, чтобы его объекты создавались следующим образом:

inp = Input(inputs)
где inputs - общее число входов (целое число). Также в объектах класса Input должен автоматически формироваться атрибут:

name = 'Input'
(Не забывайте при этом, вызывать инициализатор базового класса Layer).

Объекты второго дочернего класса Dense предполагается создавать командой:

dense = Dense(inputs, outputs, activation)
где inputs - число входов в слой; outputs - число выходов слоя (целые числа); activation - функция активации (строка, например: 'linear', 'relu', 'sigmoid'). И в каждом объекте класса Dense также должен автоматически формироваться атрибут:

name = 'Dense'
Все эти классы совместно можно использовать следующим образом (эти строчки пример, писать не нужно):

network = Input(128)
layer = network(Dense(network.inputs, 1024, 'linear'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))
Здесь создается три слоя нейронной сети.

Наконец, для перебора всех слоев с помощью цикла for, необходимо объявить отдельный класс NetworkIterator для итерирования (перебора) слоев нейронной сети следующим образом:

for x in NetworkIterator(network):
    print(x.name)
Здесь создается объект класса NetworkIterator. На вход передается первый объект (слой) нейронной сети. Объект этого класса является итератором, который в цикле for последовательно возвращает объекты (слои) нейронной сети.

P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.

'''

class Layer:
    '''Базовый класс, который образует связи между слоями.'''
    def __init__(self):
        self.next_layer = None #ссылается на следующий объект слоя нейронной сети.
        self.name = self.__class__.__name__

    def __call__(self,obj, *args, **kwargs):
        ptr = self.next_layer
        if ptr == None: #если первый объект, атрибуту next_layer присваиваем ссылку на созданный объект.
            self.next_layer = obj
        else:
            while ptr.next_layer != None: #если второй и т.д., опускаемся в конец последовательности и настраиваем связи.
                ptr = ptr.next_layer
            ptr.next_layer = obj
        return obj

    def get_list(self):
        '''Получить список слоев последовательности (пользовательский).'''
        lst = []
        lst.append(self)
        ptr = self.next_layer
        while ptr:
            lst.append(ptr)
            ptr = ptr.next_layer
        return lst


class Input(Layer):
    '''Формирование входного слоя нейронной сети.'''

    def __init__(self, inputs):
        super().__init__()
        self.inputs = inputs

class Dense(Layer):
    '''Формирование полносвязного слоя нейронной сети.'''

    def __init__(self, inputs, outputs, activation):
        super().__init__()
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation

class NetworkIterator:
    '''Отдельный класс для перебора слоев последовательности.'''

    def __init__(self, first_layer):
        self.first_layer = first_layer

    def __iter__(self):
        self.i_obj = self.first_layer
        return self

    def __next__(self):
        obj = self.i_obj
        if obj != None:
            obj_prev = obj
            self.i_obj = obj.next_layer
            return obj_prev
        else:
            raise StopIteration


# #Для проверки.
# first_layer = Layer()
# next_layer = first_layer(Layer())
# next_layer = next_layer(Layer())
#
# for obj in first_layer.get_list():
#     print(f'{id(obj)}({obj.name})-->{id(obj.next_layer)}')

network = Input(128)
layer = network(Dense(network.inputs, 1024, 'linear'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))
for x in NetworkIterator(network):
    print(x.name)

