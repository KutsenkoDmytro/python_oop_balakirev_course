'''
Объявите класс для мессенджера с именем Viber. В этом классе должны быть следующие методы:

add_message(msg) - добавление нового сообщения в список сообщений;

remove_message(msg) - удаление сообщения из списка;

set_like(msg) - поставить/убрать лайк для сообщения msg (т.е. изменить атрибут fl_like
объекта msg: если лайка нет то он ставится, если уже есть, то убирается);

show_last_message(число) - отображение последних сообщений;

total_messages() - возвращает общее число сообщений.

Эти методы предполагается использовать следующим образом (эти строчки в программе не писать):

msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)
Класс Message (необходимо также объявить) позволяет создавать объекты-сообщения со следующим набором локальных свойств:

text - текст сообщения (строка);

fl_like - поставлен или не поставлен лайк у сообщения (булево значение True - если лайк есть и False - в противном случае, изначально False);

'''

#Реализовано с использованием списков, так как сообщения могут повторяться, а словари для этого не подходят.

class Viber:
    '''Класс месенджера.'''
    __msg_list = list()

    @classmethod
    def add_message(cls, msg):
        cls.__msg_list.append(msg)

    @classmethod
    def remove_message(cls, msg):
        cls.__msg_list.remove(msg)

    @classmethod
    def set_like(cls, msg):
        if msg.fl_like:
            msg.fl_like = False
        else:
            msg.fl_like = True

    @classmethod
    def show_last_message(cls, intgr):
        print(*[msg.text for msg in cls.__msg_list[-1 * intgr:]], sep='\n')

    @classmethod
    def total_messages(cls):
        return len(cls.__msg_list)


class Message:
    '''Cоздает объекты-сообщения'''

    def __init__(self, text):
        self.text = text
        self.fl_like = False


msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)

# # Для проверки.
# Viber.show_last_message(5)
