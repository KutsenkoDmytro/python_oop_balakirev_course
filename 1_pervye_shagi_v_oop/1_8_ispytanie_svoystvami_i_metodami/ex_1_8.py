'''
Представьте, что вы получили задание от заказчика. Вас просят реализовать простую имитацию локальной сети,
состоящую из набора серверов, соединенных между собой через роутер.

Каждый сервер может отправлять пакет любому другому серверу сети. Для этого у каждого есть свой уникальный IP-адрес.
Для простоты - это просто целое (натуральное) число от 1 и до N, где N - общее число серверов.
Алгоритм следующий. Предположим, сервер с IP = 2 собирается отправить пакет информации серверу с IP = 3.
Для этого, он сначала отправляет пакет роутеру, а уже тот, смотрит на IP-адрес и пересылает пакет нужному узлу (серверу).

Для реализации этой схемы программе предлагается объявить три класса:

Server - для описания работы серверов в сети;
Router - для описания работы роутеров в сети (в данной задаче полагается один роутер);
Data - для описания пакета информации.

Серверы будут создаваться командой:

sv = Server()
При этом, уникальный IP-адрес каждого сервера должен формироваться автоматически при создании нового экземпляра класса Server.

Далее, роутер должен создаваться аналогичной командой:

router = Router()
А, пакеты данных, командой:

data = Data(строка с данными, IP-адрес назначения)
Для формирования и функционирования локальной сети, в классе Router должны быть реализованы следующие методы:

link(server) - для присоединения сервера server (объекта класса Server) к роутеру (для простоты, каждый сервер соединен только с одним роутером);
unlink(server) - для отсоединения сервера server (объекта класса Server) от роутера;
send_data() - для отправки всех пакетов (объектов класса Data) из буфера роутера соответствующим серверам (после отправки буфер должен очищаться).

И одно обязательное локальное свойство (могут быть и другие свойства):

buffer - список для хранения принятых от серверов пакетов (объектов класса Data).

Класс Server должен содержать свой набор методов:

send_data(data) - для отправки информационного пакета data (объекта класса Data) с указанным IP-адресом получателя (пакет отправляется роутеру и сохраняется в его буфере - локальном свойстве buffer);
get_data() - возвращает список принятых пакетов (если ничего принято не было, то возвращается пустой список) и очищает входной буфер;
get_ip() - возвращает свой IP-адрес.

Соответственно в объектах класса Server должны быть локальные свойства:

buffer - список принятых пакетов (объекты класса Data, изначально пустой);
ip - IP-адрес текущего сервера.

Наконец, объекты класса Data должны содержать два следующих локальных свойства:

data - передаваемые данные (строка);
ip - IP-адрес назначения.

Пример использования этих классов (эти строчки в программе писать не нужно):

router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
Ваша задача реализовать классы Router, Server и Data в соответствии с приведенным техническим заданием (ТЗ). Что-либо выводить на экран не нужно.


'''


class Server:
    '''Описывает работу серверов в сети.'''
    __ips = 0

    def __new__(cls, *args, **kwargs):
        cls.__ips += 1
        return super().__new__(cls)

    def __init__(self):
        self.ip = self.__ips
        self.buffer = list()
        self.router = None

    def send_data(self, data):
        if self.router is None:
            raise ValueError("сервер не подключен к роутеру")
        self.router.buffer.append(data)

    def get_data(self):
        clone_buffer = self.buffer.copy()
        self.buffer.clear()
        return clone_buffer

    def get_ip(self):
        return self.ip


class Router:
    '''Описывает работу роутера в сети.'''
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.servers = {}
        self.buffer = list()

    def link(self, server):
        self.servers[server.ip] = server
        server.router = self

    def unlink(self, server):
        self.servers.pop(server.ip)
        server.router = None

    def send_data(self):
        for data in self.buffer:
            if data.ip in self.servers:
                self.servers[data.ip].buffer.append(data)
        self.buffer.clear()

    # При удалении экземпляра класса, очищается атрибут класса __instance, сервера отсоидиняются от роутера
    def __del__(self):
        self.del_inst()
        for server in self.servers.values():
            server.router = None

    @classmethod
    def del_inst(cls):
        cls.__instance = None


class Data:
    '''Описывает пакет информации.'''

    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


router = Router()  # создан роутер
sv_from = Server()  # сервер отправки 1
sv_from2 = Server()  # сервер отправки 2
router.link(sv_from)  # к роутеру подключен сервер отправки 1
router.link(sv_from2)  # к роутеру подключен сервер отправки 2
router.link(Server())  # к роутеру подключен сервер без переменной 1
router.link(Server())  # к роутеру подключен сервер без переменной 2
sv_to = Server()  # сервер получения 1
router.link(sv_to)  # к роутеру подключен сервер получения 1
sv_from.send_data(Data("Hello",
                       sv_to.get_ip()))  # отправка данных в буффер роутера из сервер отправки 1 для (сервер получения 1)
sv_from2.send_data(Data("Hello",
                        sv_to.get_ip()))  # отправка данных в буффер роутера из сервер отправки 2 для (сервер получения 1)
sv_to.send_data(Data("Hi",
                     sv_from.get_ip()))  # отправка данных в буффер роутера из сервер получения 1 для (сервер отправки 1)
router.send_data()  # отправка данных из буффер роутера получателям
msg_lst_from = sv_from.get_data()  # получение списка пакетов для сервер отправки 1
msg_lst_to = sv_to.get_data()  # получение списка пакетов для сервер получения 1

# # Для проверки.
# print(msg_lst_from)
# print(msg_lst_to)
