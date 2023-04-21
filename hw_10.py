from collections import UserDict


def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return 'Not enough params. Try help'
        except ValueError:
            return 'Invalid value. Try again'
        except KeyError:
            return 'Contact not found. Try again'
    return inner


class Field:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name, phone=None):
        self.name = name
        self.phones = [phone] if phone else None

    def add_phone(self, phone):
        self.phones.append(phone)

    def change_phone(self, index, phone):
        self.phones[index] = phone

    def delete_phone(self, phone):
        self.phones.remove(phone)


class AddressBook(UserDict):

    def add_record(self, record):
        name = record.name.value
        self.data[name] = record


contacts = AddressBook()


def help(*args):
    return '''
    "hello", відповідає у консоль "How can I help you?"

    "add ...". За цією командою бот зберігає у пам'яті (у словнику наприклад) новий контакт. Замість ... 
користувач вводить ім'я та номер телефону, обов'язково через пробіл.

    "change phone..." За цією командою бот зберігає в пам'яті новий номер телефону існуючого контакту. Замість ...
 користувач вводить ім'я та номер телефону, обов'язково через пробіл.

    "phone ...." За цією командою бот виводить у консоль номер телефону для зазначеного контакту. Замість ... 
    користувач вводить ім'я контакту, чий номер треба показати.

    "show all". За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль.

    "good bye", "close", "exit" по будь-якій з цих команд бот завершує свою роботу після того, як виведе у консоль "Good bye!".
    '''


def hello(*args):
    return '''How can I help you?'''


def exit(*args):
    return '''Good Bye'''


def no_command(*args):
    return '''Unknown command, try again'''


def show_all(*args):
    return f'''{contacts}'''


@input_error
def add(*args):
    # list_of_param = args[0].split()
    name = Name(args[0])
    phone = Phone(args[1])
    record = Record(name, phone)
    # record.add_phone(phone)
    contacts.add_record(record)
    return f"Added <{name.value}> with phone <{phone.value}>"


@input_error
def phone(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    if contacts.get(name.value):
        return contacts[phone]
    return f'There are no phones with name {name}'


def change():
    ...


def show_phone_number():
    ...

COMMANDS = {help: 'help',
            add: 'add',
            exit: ['exit', 'close', 'good bye'],
            hello: 'hello',
            phone: 'phone',
            change: 'change',
            show_all: 'show all',
            show_phone_number: ' show phone'
            }


def command_handler(text):
    for command, kword in COMMANDS.items():
        if isinstance(kword, str):
            if text.lower().startswith(kword):
                return command, text.replace(kword, '').strip().split()
        elif isinstance(kword, list):
            if text.strip().lower() in kword:
                return command, None
    return no_command, None


def main():
    print(help())
    while True:
        user_input = input('>>>')
        command, data = command_handler(user_input)

        print(command(*data))

        if command == exit:
            break


if __name__ == '__main__':
    main()
