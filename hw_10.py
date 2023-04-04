from collections import UserDict


class Field:
    def __init__(self, value=None):
        self.value = value


class AddressBook(UserDict):
    def __init__(self):
        self.contacts = {}


class Record:
    class Name:
        pass

    class Phone:
        pass


# contacts = {}


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


def help(*args):
    return '''"hello", відповідає у консоль "How can I help you?"
"add ...". За цією командою бот зберігає у пам'яті (у словнику наприклад) новий контакт. Замість ... користувач вводить ім'я та номер телефону, обов'язково через пробіл.
"change ..." За цією командою бот зберігає в пам'яті новий номер телефону існуючого контакту. Замість ... користувач вводить ім'я та номер телефону, обов'язково через пробіл.
"phone ...." За цією командою бот виводить у консоль номер телефону для зазначеного контакту. Замість ... користувач вводить ім'я контакту, чий номер треба показати.
"show all". За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль.
"good bye", "close", "exit" по будь-якій з цих команд бот завершує свою роботу після того, як виведе у консоль "Good bye!".'''


@input_error
def add(*args):
    list_of_param = args[0].split()
    name = list_of_param[1]
    phone = list_of_param[2]
    contacts[name] = phone

    if not phone:
        raise IndexError()

    return f'''name - {name}, phone - {phone}'''


def hello(*args):
    return '''How can I help you?'''


def exit(*args):
    return '''Good Bye'''


def no_command(*args):
    return '''Unknown command, try again'''


@input_error
def phone(*args):
    list_of_param = args[0].split()
    name = list_of_param[0]
    return f'''{name} phone is {contacts[name]}'''


def show_all(*args):
    return f'''{contacts}'''


@input_error
def change(*args):
    list_of_param = args[0].split()
    name = list_of_param[0]
    new_phone = list_of_param[1]
    contacts.update({name: new_phone})
    return f'''{name} new phone is {new_phone}'''


COMMANDS = {help: 'help',
            add: 'add',
            exit: ['exit', 'close', 'good bye'],
            hello: 'hello',
            change: 'change',
            phone: 'phone',
            show_all: 'show all'
            }


def command_handler(text):
    for command, kword in COMMANDS.items():
        if isinstance(kword, str):
            if text.lower().startswith(kword):
                return command, text.replace(kword, '').strip()
        elif isinstance(kword, list):
            if text.strip().lower() in kword:
                return command, None


def main():
    print(help())
    while True:
        user_input = input('>>>')
        command, data = command_handler(user_input)

        print(command(data))

        if command == exit:
            break


if __name__ == '__main__':
    main()
